import{aL as d,al as X,b8 as v,c as m,u as A,af as x,aS as L,l as b,s as K,r as q,o as R,an as k,ao as h,F as w,aQ as H,a9 as W,ac as z,aN as T,aM as M,e as $,E,S as ee}from"./@vue-e16f66a9.js";import{c as te}from"./pinia-9fcab373.js";import{d as oe}from"./dayjs-7e8bcc51.js";import{R as y,u as Q,a as ne,c as ae,b as se}from"./vue-router-c7505a30.js";import{C as Y,z as B,_ as V,L as re,a as ie,b as ce,n as O,c as le,B as ue}from"./ant-design-vue-a65eb274.js";import{N as Z}from"./nprogress-733e006c.js";import{a as pe}from"./axios-cd074bab.js";import"./@babel-5c3af8a7.js";import"./@ant-design-b54d9c65.js";import"./@ctrl-eebb6dbe.js";import"./resize-observer-polyfill-2974a3e4.js";import"./lodash-es-26de6f87.js";import"./async-validator-dee29e8b.js";import"./scroll-into-view-if-needed-7942c886.js";import"./compute-scroll-into-view-183f845a.js";import"./vue-types-ef06c517.js";import"./dom-align-529d0cdc.js";import"./form-data-d2a9677b.js";(function(){const n=document.createElement("link").relList;if(n&&n.supports&&n.supports("modulepreload"))return;for(const e of document.querySelectorAll('link[rel="modulepreload"]'))c(e);new MutationObserver(e=>{for(const o of e)if(o.type==="childList")for(const i of o.addedNodes)i.tagName==="LINK"&&i.rel==="modulepreload"&&c(i)}).observe(document,{childList:!0,subtree:!0});function a(e){const o={};return e.integrity&&(o.integrity=e.integrity),e.referrerpolicy&&(o.referrerPolicy=e.referrerpolicy),e.crossorigin==="use-credentials"?o.credentials="include":e.crossorigin==="anonymous"?o.credentials="omit":o.credentials="same-origin",o}function c(e){if(e.ep)return;e.ep=!0;const o=a(e);fetch(e.href,o)}})();const me={__name:"App",setup(t,{expose:n}){return n({RouterView:y,ConfigProvider:Y,zh_CN:B}),(a,c)=>(d(),X(A(Y),{locale:A(B)},{default:v(()=>[m(A(y),null,{default:v(({Component:e})=>[(d(),X(x,null,[(d(),X(L(e)))],1024))]),_:1})]),_:1},8,["locale"]))}},de="modulepreload",he=function(t){return"/static/"+t},P={},_=function(n,a,c){if(!a||a.length===0)return n();const e=document.getElementsByTagName("link");return Promise.all(a.map(o=>{if(o=he(o),o in P)return;P[o]=!0;const i=o.endsWith(".css"),u=i?'[rel="stylesheet"]':"";if(!!c)for(let s=e.length-1;s>=0;s--){const r=e[s];if(r.href===o&&(!i||r.rel==="stylesheet"))return}else if(document.querySelector(`link[href="${o}"]${u}`))return;const l=document.createElement("link");if(l.rel=i?"stylesheet":de,i||(l.as="script",l.crossOrigin=""),l.href=o,document.head.appendChild(l),i)return new Promise((s,r)=>{l.addEventListener("load",s),l.addEventListener("error",()=>r(new Error(`Unable to preload CSS for ${o}`)))})})).then(()=>n())},ge="data:image/png;base64,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";const S=(t,n)=>{const a=t.__vccOpts||t;for(const[c,e]of n)a[c]=e;return a},F=t=>(T("data-v-c675c7ae"),t=t(),M(),t),_e={class:"nav-wrap"},fe=F(()=>h("div",{class:"logo"},[h("img",{src:ge,alt:"logo"})],-1)),be={class:"tab-panel"},ve=["onClick"],Ne={class:"menu-wrap"},Xe={class:"com-icon"},ke=F(()=>h("span",{style:{"margin-left":"6px"}},"欢迎您，",-1)),Ae={__name:"CustomNav",setup(t,{expose:n}){const a=Q(),c=ne(),e=b("/home/grkh");K(()=>{c.meta&&c.meta.tabActive&&(e.value=c.meta.tabActive)});function o(r){a.push({path:r})}const i=q([{name:"个人客户",path:"/home/grkh"},{name:"机构客户",path:"/home/jgkh"},{name:"操作日志",path:"/home/log"}]),u=b(""),f=b([]),l=b([]),s=r=>{let p=f.value.find(N=>N.id===r);localStorage.setItem("currentUser",JSON.stringify(p))};return R(()=>{let r=JSON.parse(localStorage.getItem("currentUser"));f.value=JSON.parse(localStorage.getItem("userList")),u.value=r.id,l.value=f.value.map(p=>({label:p.name,value:p.id}))}),n({currentUser:u,options:l,tabList:i,activeKey:e,handleChange:s,handleTabClick:o}),(r,p)=>{const N=V;return d(),k("div",_e,[fe,h("ul",be,[(d(!0),k(w,null,H(i,g=>(d(),k("li",{class:W(["tab-item",[e.value===g.path?"active":""]]),key:g.path,onClick:J=>o(g.path)},z(g.name),11,ve))),128))]),h("div",Ne,[h("span",Xe,[ke,m(N,{ref:"select",value:u.value,"onUpdate:value":p[0]||(p[0]=g=>u.value=g),style:{width:"120px"},options:l.value,onChange:s},null,8,["value","options"])])])])}}},U=S(Ae,[["__scopeId","data-v-c675c7ae"]]);const ye={__name:"Home",setup(t,{expose:n}){return n({RouterView:y,CustomNav:U}),(a,c)=>{const e=re,o=ie,i=ce;return d(),k(w,null,[m(o,null,{default:v(()=>[m(U),m(e,{class:"router-view"},{default:v(()=>[m(A(y),null,{default:v(({Component:u})=>[(d(),X(x,null,[(d(),X(L(u)))],1024))]),_:1})]),_:1})]),_:1}),m(i)],64)}}},Oe=S(ye,[["__scopeId","data-v-6343381c"]]),je="/static/png/login-banner-64de137a.png",Se="http://localhost:8000/api/v1/",D={baseUrl:Se,operators:"operators",customersList:"customers",customersRemind:"customers/remind/count",contacts:"contacts",funds:"funds",cooperations:"cooperations",logs:"logs",exportLogs:"logs/export"};const G=t=>(T("data-v-2b7d3197"),t=t(),M(),t),Ce={class:"page"},Ie=G(()=>h("img",{class:"login-banner",src:je,alt:"banner"},null,-1)),Je={class:"login-wrap"},Ee=G(()=>h("h2",{class:"login-title"},"基金客户管理系统",-1)),Ye={__name:"Login",setup(t,{expose:n}){const a=$("$http"),c=Q(),e=b(""),o=b([]),i=b([]),u=s=>{let r=o.value.find(p=>p.id===s);localStorage.setItem("currentUser",JSON.stringify(r))},f=()=>{e.value!==""&&e.value!==void 0&&e.value!==null?c.replace({path:"/home"}):O.warn({message:"温馨提示",description:"请先选择用户"})},l=async()=>{const{data:s}=await a.get(D.operators,{params:{pageNo:1,paseSize:100}});o.value=s,localStorage.setItem("userList",JSON.stringify(s)),i.value=s.map(r=>({label:r.name,value:r.id})),s&&s.length>0&&(localStorage.setItem("currentUser",JSON.stringify(s[0])),e.value=s[0].id)};return R(()=>{l()}),n({currentUser:e,options:i,login:f,handleChange:u}),(s,r)=>{const p=le,N=V,g=ue;return d(),k("div",Ce,[h("main",null,[Ie,h("div",Je,[m(p,{level:2},{default:v(()=>[E("欢迎登录")]),_:1}),Ee,m(N,{class:"login-select",size:"large",value:e.value,"onUpdate:value":r[0]||(r[0]=J=>e.value=J),placeholder:"请选择登录用户",options:i.value,onChange:u},null,8,["value","options"]),m(g,{type:"primary",block:"",style:{height:"50px"},onClick:f},{default:v(()=>[E("登录")]),_:1})])])])}}},Be=S(Ye,[["__scopeId","data-v-2b7d3197"]]),C=ae({history:se("/static/"),routes:[{path:"/",redirect:"/login"},{path:"/login",component:Be},{path:"/home",name:"home",redirect:"/home/grkh",component:Oe,children:[{path:"grkh",meta:{tabActive:"/home/grkh"},name:"grkh",component:()=>_(()=>import("./ConsumerClientList-6a72dbe2.js"),["js/ConsumerClientList-6a72dbe2.js","js/ant-design-vue-a65eb274.js","js/@babel-5c3af8a7.js","js/@vue-e16f66a9.js","js/@ant-design-b54d9c65.js","js/@ctrl-eebb6dbe.js","js/resize-observer-polyfill-2974a3e4.js","js/lodash-es-26de6f87.js","js/async-validator-dee29e8b.js","js/scroll-into-view-if-needed-7942c886.js","js/compute-scroll-into-view-183f845a.js","js/dayjs-7e8bcc51.js","js/vue-types-ef06c517.js","js/dom-align-529d0cdc.js","css/ant-design-vue-9db73ac6.css","js/vue-router-c7505a30.js","js/store-7a36e7d0.js","js/pinia-9fcab373.js","js/ColumnSetting-6413dc10.js","js/vuedraggable-bd7afe23.js","js/vue-5ceb0fee.js","js/sortablejs-55e3eda9.js","css/ColumnSetting-c0d65122.css","js/nprogress-733e006c.js","css/nprogress-8b89e2e0.css","js/axios-cd074bab.js","js/form-data-d2a9677b.js","css/ConsumerClientList-ed8f096f.css"])},{path:"grkhForm",meta:{tabActive:"/home/grkh"},name:"grkhForm",component:()=>_(()=>import("./ConsumerClientForm-e4a8c29b.js"),["js/ConsumerClientForm-e4a8c29b.js","js/ant-design-vue-a65eb274.js","js/@babel-5c3af8a7.js","js/@vue-e16f66a9.js","js/@ant-design-b54d9c65.js","js/@ctrl-eebb6dbe.js","js/resize-observer-polyfill-2974a3e4.js","js/lodash-es-26de6f87.js","js/async-validator-dee29e8b.js","js/scroll-into-view-if-needed-7942c886.js","js/compute-scroll-into-view-183f845a.js","js/dayjs-7e8bcc51.js","js/vue-types-ef06c517.js","js/dom-align-529d0cdc.js","css/ant-design-vue-9db73ac6.css","js/vue-router-c7505a30.js","js/store-7a36e7d0.js","js/pinia-9fcab373.js","js/ProductDetailTable-46627c71.js","css/ProductDetailTable-2b960192.css","js/nprogress-733e006c.js","css/nprogress-8b89e2e0.css","js/axios-cd074bab.js","js/form-data-d2a9677b.js","css/ConsumerClientForm-ac21e9f0.css"])},{path:"grkhDetail",meta:{tabActive:"/home/grkh"},name:"grkhDetail",component:()=>_(()=>import("./ConsumerClientDetail-21ddc9f8.js"),["js/ConsumerClientDetail-21ddc9f8.js","js/ant-design-vue-a65eb274.js","js/@babel-5c3af8a7.js","js/@vue-e16f66a9.js","js/@ant-design-b54d9c65.js","js/@ctrl-eebb6dbe.js","js/resize-observer-polyfill-2974a3e4.js","js/lodash-es-26de6f87.js","js/async-validator-dee29e8b.js","js/scroll-into-view-if-needed-7942c886.js","js/compute-scroll-into-view-183f845a.js","js/dayjs-7e8bcc51.js","js/vue-types-ef06c517.js","js/dom-align-529d0cdc.js","css/ant-design-vue-9db73ac6.css","js/vue-router-c7505a30.js","js/store-7a36e7d0.js","js/pinia-9fcab373.js","js/ProductDetailTable-46627c71.js","css/ProductDetailTable-2b960192.css","js/nprogress-733e006c.js","css/nprogress-8b89e2e0.css","js/axios-cd074bab.js","js/form-data-d2a9677b.js","css/ConsumerClientDetail-3b587f35.css"])},{path:"jgkh",meta:{tabActive:"/home/jgkh"},name:"jgkh",component:()=>_(()=>import("./InstitutionalClientList-751e3cba.js"),["js/InstitutionalClientList-751e3cba.js","js/ant-design-vue-a65eb274.js","js/@babel-5c3af8a7.js","js/@vue-e16f66a9.js","js/@ant-design-b54d9c65.js","js/@ctrl-eebb6dbe.js","js/resize-observer-polyfill-2974a3e4.js","js/lodash-es-26de6f87.js","js/async-validator-dee29e8b.js","js/scroll-into-view-if-needed-7942c886.js","js/compute-scroll-into-view-183f845a.js","js/dayjs-7e8bcc51.js","js/vue-types-ef06c517.js","js/dom-align-529d0cdc.js","css/ant-design-vue-9db73ac6.css","js/vue-router-c7505a30.js","js/store-7a36e7d0.js","js/pinia-9fcab373.js","js/ColumnSetting-6413dc10.js","js/vuedraggable-bd7afe23.js","js/vue-5ceb0fee.js","js/sortablejs-55e3eda9.js","css/ColumnSetting-c0d65122.css","js/nprogress-733e006c.js","css/nprogress-8b89e2e0.css","js/axios-cd074bab.js","js/form-data-d2a9677b.js","css/InstitutionalClientList-660175f4.css"])},{path:"jgkhForm",meta:{tabActive:"/home/jgkh"},name:"jgkhForm",component:()=>_(()=>import("./InstitutionalClientForm-d64e3ce1.js"),["js/InstitutionalClientForm-d64e3ce1.js","js/ant-design-vue-a65eb274.js","js/@babel-5c3af8a7.js","js/@vue-e16f66a9.js","js/@ant-design-b54d9c65.js","js/@ctrl-eebb6dbe.js","js/resize-observer-polyfill-2974a3e4.js","js/lodash-es-26de6f87.js","js/async-validator-dee29e8b.js","js/scroll-into-view-if-needed-7942c886.js","js/compute-scroll-into-view-183f845a.js","js/dayjs-7e8bcc51.js","js/vue-types-ef06c517.js","js/dom-align-529d0cdc.js","css/ant-design-vue-9db73ac6.css","js/vue-router-c7505a30.js","js/store-7a36e7d0.js","js/pinia-9fcab373.js","js/ProductDetailTable-46627c71.js","css/ProductDetailTable-2b960192.css","js/DiscountSalerTable-b7b4bad3.js","css/DiscountSalerTable-e01cffcc.css","js/nprogress-733e006c.js","css/nprogress-8b89e2e0.css","js/axios-cd074bab.js","js/form-data-d2a9677b.js","css/InstitutionalClientForm-b81be9e4.css"])},{path:"jgkhDetail",meta:{tabActive:"/home/jgkh"},name:"jgkhDetail",component:()=>_(()=>import("./InstitutionalClientDetail-b1837202.js"),["js/InstitutionalClientDetail-b1837202.js","js/ant-design-vue-a65eb274.js","js/@babel-5c3af8a7.js","js/@vue-e16f66a9.js","js/@ant-design-b54d9c65.js","js/@ctrl-eebb6dbe.js","js/resize-observer-polyfill-2974a3e4.js","js/lodash-es-26de6f87.js","js/async-validator-dee29e8b.js","js/scroll-into-view-if-needed-7942c886.js","js/compute-scroll-into-view-183f845a.js","js/dayjs-7e8bcc51.js","js/vue-types-ef06c517.js","js/dom-align-529d0cdc.js","css/ant-design-vue-9db73ac6.css","js/vue-router-c7505a30.js","js/store-7a36e7d0.js","js/pinia-9fcab373.js","js/ProductDetailTable-46627c71.js","css/ProductDetailTable-2b960192.css","js/DiscountSalerTable-b7b4bad3.js","css/DiscountSalerTable-e01cffcc.css","js/nprogress-733e006c.js","css/nprogress-8b89e2e0.css","js/axios-cd074bab.js","js/form-data-d2a9677b.js","css/InstitutionalClientDetail-685b8886.css"])},{path:"log",meta:{tabActive:"/home/log"},name:"log",component:()=>_(()=>import("./OperationLogList-e8a5e4bf.js"),["js/OperationLogList-e8a5e4bf.js","js/ant-design-vue-a65eb274.js","js/@babel-5c3af8a7.js","js/@vue-e16f66a9.js","js/@ant-design-b54d9c65.js","js/@ctrl-eebb6dbe.js","js/resize-observer-polyfill-2974a3e4.js","js/lodash-es-26de6f87.js","js/async-validator-dee29e8b.js","js/scroll-into-view-if-needed-7942c886.js","js/compute-scroll-into-view-183f845a.js","js/dayjs-7e8bcc51.js","js/vue-types-ef06c517.js","js/dom-align-529d0cdc.js","css/ant-design-vue-9db73ac6.css","js/pinia-9fcab373.js","js/vue-router-c7505a30.js","js/nprogress-733e006c.js","css/nprogress-8b89e2e0.css","js/axios-cd074bab.js","js/form-data-d2a9677b.js","css/OperationLogList-6445a199.css"])}]},{path:"/404",name:"404",component:()=>_(()=>import("./NotFound-fa70a503.js"),["js/NotFound-fa70a503.js","js/ant-design-vue-a65eb274.js","js/@babel-5c3af8a7.js","js/@vue-e16f66a9.js","js/@ant-design-b54d9c65.js","js/@ctrl-eebb6dbe.js","js/resize-observer-polyfill-2974a3e4.js","js/lodash-es-26de6f87.js","js/async-validator-dee29e8b.js","js/scroll-into-view-if-needed-7942c886.js","js/compute-scroll-into-view-183f845a.js","js/dayjs-7e8bcc51.js","js/vue-types-ef06c517.js","js/dom-align-529d0cdc.js","css/ant-design-vue-9db73ac6.css","js/vue-router-c7505a30.js"])},{path:"/:pathMatch(.*)*",redirect:"/404"}],scrollBehavior(){return{top:0}}});C.beforeEach((t,n,a)=>{if(Z.start(),t.path==="/login")return a();t.matched.length===0&&a("/404");const c=JSON.parse(localStorage.getItem("currentUser"));if(!c||c.id==="")return O.error({message:"温馨提示",description:"您还未选择当前用户"}),a("/login");a()});C.afterEach(()=>{Z.done()});const Pe=D.baseUrl,I=pe.create({baseURL:Pe,timeout:6e4,withCredentials:!1,headers:{"Content-Type":"application/json"}});I.interceptors.request.use(t=>{const n=JSON.parse(localStorage.getItem("currentUser"));return n&&n.id&&(t.headers["operator-id"]=n.id),t},t=>(O.error({message:"温馨提示",description:"网络请求失败"}),Promise.reject(t)));I.interceptors.response.use(t=>t.data,t=>{var n,a;return O.error({message:"温馨提示",description:((a=(n=t.response)==null?void 0:n.data)==null?void 0:a.message)||t.message}),Promise.reject(t)});oe.locale("zh-cn");const j=ee(me);j.use(te());j.use(C);j.provide("$http",I);j.mount("#app");export{S as _,D as a};