/*
 * MxsDoc 官网统计加载器（provider-agnostic）
 * ------------------------------------------------------------------
 * 设计原则：
 *   1. 零配置时完全空转（不发起任何网络请求），不拖慢首屏。
 *   2. 不写 cookie、不做跨站追踪、不采集 PII、不做设备指纹。
 *   3. 遵守浏览器 DNT (Do Not Track) 与 GPC (Global Privacy Control)。
 *   4. provider 无关：填哪家就加载哪家，业务代码零改动。
 *
 * ------------------------------------------------------------------
 * 启用方式（编辑本文件下方 CONFIG，或在任一页面 <head> 内先定义
 * window.MXS_ANALYTICS_CONFIG 覆盖）：
 *
 *   <script>
 *     window.MXS_ANALYTICS_CONFIG = {
 *       ga4Id: 'G-XXXXXXXXXX',        // Google Analytics 4
 *       plausibleDomain: 'mxsdoc.cn', // Plausible（自建或 Cloud）
 *       umamiWebsiteId: 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx', // Umami
 *       umamiSrc: 'https://cloud.umami.is', // Umami 自建实例地址
 *       relayUrl: ''                  // 自有中继：POST JSON 到你自己的服务端
 *     };
 *   </script>
 *   <script src="/mxsdoc-site/assets/js/analytics.js" defer></script>
 *
 * relayUrl 会发送的字段（仅此五项，无 IP 落库、无 cookie、无标识符）：
 *   { path, referrer, lang, viewport, ts }
 *   path      当前页面路径（含 query，便于看 AI 爬虫抓取分布）
 *   referrer  来源页（判断是否来自 ChatGPT / Perplexity 等 AI 入口）
 *   lang      navigator.language
 *   viewport  视口宽 x 高
 *   ts        客户端时间戳（ISO 8601）
 *
 * relayUrl 服务端务必自行决定是否记录 IP 与如何留存，本脚本不代劳。
 * ------------------------------------------------------------------
 */
(function () {
  'use strict';

  var CONFIG = {
    ga4Id: '',
    plausibleDomain: '',
    umamiWebsiteId: '',
    umamiSrc: 'https://cloud.umami.is',
    relayUrl: ''
  };

  // 允许页面在加载本脚本前定义配置以覆盖默认值
  if (window.MXS_ANALYTICS_CONFIG && typeof window.MXS_ANALYTICS_CONFIG === 'object') {
    for (var k in CONFIG) {
      if (Object.prototype.hasOwnProperty.call(window.MXS_ANALYTICS_CONFIG, k)) {
        var v = window.MXS_ANALYTICS_CONFIG[k];
        if (typeof v === 'string') CONFIG[k] = v;
      }
    }
  }

  // ---- 隐私开关：用户明确拒绝就一票不发 ----------------------------
  function optedOut() {
    var dnt = navigator.doNotTrack === '1' ||
              window.doNotTrack === '1' ||
              navigator.msDoNotTrack === '1';
    var gpc = false;
    try {
      gpc = navigator.globalPrivacyControl === true;
    } catch (e) { /* 老浏览器无此属性 */ }
    return dnt || gpc;
  }

  if (optedOut()) return;

  var loaded = [];
  function loadScript(src) {
    if (loaded.indexOf(src) !== -1) return;
    loaded.push(src);
    var s = document.createElement('script');
    s.async = true;
    s.src = src;
    document.head.appendChild(s);
  }

  function currentPath() {
    return window.location.pathname + window.location.search;
  }

  // ---- GA4 -----------------------------------------------------------
  if (CONFIG.ga4Id) {
    loadScript('https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(CONFIG.ga4Id));
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', CONFIG.ga4Id, {
      anonymize_ip: true,
      send_page_view: true,
      cookie_flags: 'SameSite=None;Secure'
    });
  }

  // ---- Plausible -----------------------------------------------------
  // 官方写法：站点域名作为 data-domain，脚本自动上报 pageview
  if (CONFIG.plausibleDomain) {
    loadScript('https://plausible.io/js/script.js');
    window.plausible = window.plausible || function () {
      (window.plausible.q = window.plausible.q || []).push(arguments);
    };
    window.plausible('pageview', { props: { path: currentPath() } });
  }

  // ---- Umami ---------------------------------------------------------
  if (CONFIG.umamiWebsiteId) {
    var src = CONFIG.umamiSrc.replace(/\/+$/, '');
    loadScript(src + '/script.js');
    window.umami = window.umami || {};
    window.umami.websiteId = CONFIG.umamiWebsiteId;
  }

  // ---- 自有中继（无 cookie / 无标识符） --------------------------------
  if (CONFIG.relayUrl) {
    var payload = {
      path: currentPath(),
      referrer: document.referrer || '',
      lang: navigator.language || '',
      viewport: window.innerWidth + 'x' + window.innerHeight,
      ts: new Date().toISOString()
    };
    try {
      if (navigator.sendBeacon) {
        var blob = new Blob([JSON.stringify(payload)], { type: 'application/json' });
        navigator.sendBeacon(CONFIG.relayUrl, blob);
      } else {
        fetch(CONFIG.relayUrl, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload),
          keepalive: true
        }).catch(function () { /* 统计失败不影响浏览 */ });
      }
    } catch (e) {
      /* 统计失败绝不阻断页面 */
    }
  }
})();
