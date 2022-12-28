import{m as ke,p as Pe,q as $e,r as Ne,I as Ve,h as Le,i as ze,_ as Ae,j as He,s as Ie,t as Ke,B as Xe,D as Ze,R as Ge,u as Je,F as Qe,S as We,w as ea}from"./ant-design-vue-69c5e787.js";import{e as aa,l as _,K as la,r as f,s as U,X as v,a0 as w,c as e,Z as l,F as C,u as ta,E as p,a6 as O,a4 as Y,t as L,A as z,Y as x,B as Q,a7 as na,a1 as W}from"./@vue-0057e33b.js";import{a as ua,u as oa}from"./vue-router-2c461628.js";import{s as sa}from"./pinia-75b29db1.js";import{u as ra}from"./store-b4c7e3e8.js";import{a as ye}from"./index-a7c45ba7.js";import{C as Me,P as Ue}from"./ProductDetailTable-002d87ee.js";import{D as we}from"./DiscountSalerTable-cb29639e.js";import{d as A}from"./dayjs-d2af4db4.js";import{H as Ce}from"./@ant-design-c5cfb3ae.js";import"./@babel-f2deaedd.js";import"./lodash-es-c37e40cf.js";import"./resize-observer-polyfill-2974a3e4.js";import"./async-validator-dee29e8b.js";import"./scroll-into-view-if-needed-7942c886.js";import"./compute-scroll-into-view-183f845a.js";import"./vue-types-ef06c517.js";import"./@ctrl-eebb6dbe.js";import"./dom-align-529d0cdc.js";import"./nprogress-8c52ea9a.js";import"./axios-cd074bab.js";import"./form-data-d2a9677b.js";const ia=W("h3",{class:"form-title"},"基本信息",-1),_a=W("h3",{class:"form-title"},"客户归属",-1),da=W("h3",{class:"form-title"},"融资融券",-1),Fa={__name:"InstitutionalClientForm",setup(va,{expose:Oe}){const ee=aa("$http"),H=ua(),xe=oa();function ae(){xe.back()}const F=_("add"),Ee=ra(),{jgkhForm:le}=sa(Ee);la(()=>{H.query&&(F.value=H.query.type,H.query.type==="edit"?je():I())});const I=()=>{K.value.resetFields(),M.value=[],y.value=[],m.value=[],E.value="",c.value=[],j.value="",k.value=[],b.value=[],D.value="",g.value=[],R.value=""},je=()=>{Object.keys(le.value).filter(u=>u!=="updated_at"&&u!=="created_at").forEach(u=>{const a=le.value[u];switch(u){case"private_placement_strategy":Object.keys(a).forEach(r=>{a[r]&&m.value.push(r),r==="other"&&(E.value=a[r])});break;case"fund_demand":Object.keys(a).forEach(r=>{a[r]&&c.value.push(r),r==="other"&&(j.value=a[r])});break;case"technical_demand":Object.keys(a).forEach(r=>{a[r]&&k.value.push(r)});break;case"bond_source_demand":Object.keys(a).forEach(r=>{a[r]&&b.value.push(r),r==="other"&&(D.value=a[r])});break;case"investment_research_demand":Object.keys(a).forEach(r=>{a[r]&&g.value.push(r),r==="other"&&(R.value=a[r])});break;case"permissions":Object.keys(a).forEach(r=>{a[r]&&y.value.push(r)});break;case"interest_rate_effective_date":M.value[0]=A(a,T);break;case"interest_rate_expiry_date":M.value[1]=A(a,T);break;default:n[u]=a;break}})},K=_(),n=f({customer_type:1}),te=f([{label:"男",value:0},{label:"女",value:1}]),ne=f([{key:"0-5亿",value:"0-5E"},{key:"5-10亿",value:"5-10E"},{key:"10-20亿",value:"10-20E"},{key:"20-50亿",value:"20-50E"},{key:"50-100亿",value:"50-100E"},{key:"100亿以上",value:">100E"}]),P=_(null);function ue(){P.value.openModal(n.id)}function X(){P.value.closeModal()}function oe(){X()}const $=_(null);function se(){$.value.openModal(n.id)}function Z(){$.value.closeModal()}function re(){Z()}const N=_(null);function ie(){N.value.openModal(n.id)}function G(){N.value.closeModal()}function _e(){G()}const m=_([]),E=_(""),de=f([{label:"主观多头",value:"subjective_long_position"},{label:"量化多头",value:"quantifying_long_positions"},{label:"中性策略",value:"neutral_strategy"},{label:"套利策略",value:"arbitrage_strategy"},{label:"期货/期权",value:"forward_option"},{label:"多策略",value:"multi_strategy"},{label:"其他",value:"other"}]);U(()=>{if(m.value&&m.value.length){const u={};m.value.forEach(a=>{a!=="other"?u[a]=!0:u[a]=E.value}),n.private_placement_strategy=u}});const c=_([]),j=_(""),ve=f([{label:"代销",value:"sale_by_proxy"},{label:"其他",value:"other"}]);U(()=>{if(c.value&&c.value.length){const u={};c.value.forEach(a=>{a!=="other"?u[a]=!0:u[a]=j.value}),n.fund_demand=u}});const k=_([]),pe=f([{label:"需要特定柜台",value:"is_need_specific_counter"},{label:"需要极速行情",value:"is_need_top_speed_market"},{label:"需要定制化",value:"is_need_customization"},{label:"有三方算法需求",value:"is_need_tripartite_algorithms"}]);U(()=>{if(k.value&&k.value.length){const u={};k.value.forEach(a=>{u[a]=!0}),n.technical_demand=u}});const b=_([]),D=_(""),fe=f([{label:"行业篮子股票券源",value:"sector_basket_stocks"},{label:"宽基篮子股票券源",value:"wide_base_basket_stocks"},{label:"个股券源",value:"individual_share"},{label:"其他",value:"other"}]);U(()=>{if(b.value&&b.value.length){const u={};b.value.forEach(a=>{a!=="other"?u[a]=!0:u[a]=D.value}),n.bond_source_demand=u}});const g=_([]),R=_(""),me=f([{label:"研究所研报",value:"research_report_of_the_institute"},{label:"研究所白名单",value:"research_institute_whitelist"},{label:"研究所年费服务",value:"institute_annual_fee_service"},{label:"参与研究所路演",value:"participate_in_the_institute_road_show"},{label:"其他",value:"other"}]);U(()=>{if(g.value&&g.value.length){const u={};g.value.forEach(a=>{a!=="other"?u[a]=!0:u[a]=R.value}),n.investment_research_demand=u}});const ce=f([{label:"保守型",value:"保守型"},{label:"稳健型",value:"稳健型"},{label:"平衡型",value:"平衡型"},{label:"积极型",value:"积极型"},{label:"激进型",value:"激进型"}]),be=f([{label:"是",value:1},{label:"否",value:0}]),y=_([]),ge=f([{label:"现金宝",value:"cash_treasure"},{label:"基金定投",value:"automatic_investment_plan"},{label:"双创板",value:"double_innovation_board"},{label:"期权",value:"share_option"},{label:"深港通",value:"shenzhen_hong_kong_stock_connect"},{label:"沪港通",value:"shanghai_hong_kong_stock_connect"},{label:"两融账户",value:"double_margin_account"},{label:"北交所",value:"beijing_stock_exchange"}]);U(()=>{if(y.value&&y.value.length){const u={};y.value.forEach(a=>{u[a]=!0}),n.permissions=u}});const M=_([]),T="YYYY-MM-DD";U(()=>{M.value&&(n.interest_rate_effective_date=A(M.value[0]).format(T),n.interest_rate_expiry_date=A(M.value[1]).format(T))});const V=_(!1),he=()=>{V.value=!0,F.value==="add"?ee.post(ye.customersList,{...n}).then(u=>{u.code===0&&(ke.success("新增成功"),I())}).finally(()=>{V.value=!1}):ee.put(`${ye.customersList}/${n.id}`,{...n}).then(u=>{u.code===0&&ke.success("编辑成功")}).finally(()=>{V.value=!1})};return Oe({HomeOutlined:Ce,operateType:F,formRef:K,formState:n,genderOptions:te,risk_appetite_options:ce,dateFormat:T,permissions:y,permissionOptions:ge,private_placement_strategy:m,private_placement_strategy_other:E,private_placement_strategy_options:de,fund_demand:c,fund_demand_other:j,fund_demand_options:ve,technical_demand:k,technical_demand_options:pe,bond_source_demand:b,bond_source_demand_other:D,bond_source_demand_options:fe,investment_research_demand:g,investment_research_demand_other:R,investment_research_demand_options:me,scale_of_management_options:ne,is_internet_channel_options:be,ContactDetailTable:Me,ProductDetailTable:Ue,DiscountSalerTable:we,contactRef:P,fundsRef:$,cooperationsRef:N,back:ae,onFinish:he,handleContactDetailShow:ue,handleContactTableOk:oe,handleContactTableCancel:X,handleProductTableShow:se,handleProductTableCancel:Z,handleProductTableOk:re,handleDiscountTableShow:ie,handleDiscountTableCancel:G,handleDiscountTableOk:_e}),(u,a)=>{const r=Ne,De=Pe,i=Ve,s=Le,o=ze,Re=We,Te=Ae,d=He,J=Ie,q=ea,S=Ke,B=Xe,Se=Ze,Ye=Ge,Fe=Je,qe=Qe,Be=$e;return v(),w(C,null,[e(De,null,{default:l(()=>[e(r,{onClick:ae},{default:l(()=>[e(ta(Ce))]),_:1}),e(r,null,{default:l(()=>[p("机构客户"+O(F.value==="add"?"新增":"编辑"),1)]),_:1})]),_:1}),e(Be,{spinning:V.value,tip:"正在提交..."},{default:l(()=>[e(qe,{ref_key:"formRef",ref:K,name:"advanced_search",class:"ant-advanced-search-form",model:n,onFinish:he},{default:l(()=>[ia,e(d,{gutter:24},{default:l(()=>[e(o,{span:8},{default:l(()=>[e(s,{name:"capital_account",label:"私募编码",rules:[{required:!0,message:"请输入私募编码"}]},{default:l(()=>[e(i,{value:n.capital_account,"onUpdate:value":a[0]||(a[0]=t=>n.capital_account=t),valueModifiers:{trim:!0}},null,8,["value"])]),_:1})]),_:1}),e(o,{span:8},{default:l(()=>[e(s,{name:"name",label:"机构名称",rules:[{required:!0,message:"请输入机构名称"}]},{default:l(()=>[e(i,{value:n.name,"onUpdate:value":a[1]||(a[1]=t=>n.name=t),valueModifiers:{trim:!0}},null,8,["value"])]),_:1})]),_:1}),e(o,{span:8},{default:l(()=>[e(s,{name:"scale_of_management",label:"管理规模",rules:[{required:!0,message:"请输入管理规模"}]},{default:l(()=>[e(Te,{value:n.scale_of_management,"onUpdate:value":a[2]||(a[2]=t=>n.scale_of_management=t),placeholder:"请选择"},{default:l(()=>[(v(!0),w(C,null,Y(ne,t=>(v(),x(Re,{key:t.value,value:t.value},{default:l(()=>[p(O(t.key),1)]),_:2},1032,["value"]))),128))]),_:1},8,["value"])]),_:1})]),_:1})]),_:1}),e(d,{gutter:24},{default:l(()=>[e(o,{span:8},{default:l(()=>[e(s,{name:"contact_person",label:"联 系 人",rules:[{required:!0,message:"请输入联系人"}]},{default:l(()=>[e(i,{value:n.contact_person,"onUpdate:value":a[3]||(a[3]=t=>n.contact_person=t),valueModifiers:{trim:!0}},null,8,["value"])]),_:1})]),_:1}),e(o,{span:8},{default:l(()=>[e(s,{name:"gender",label:"性  别",rules:[{required:!0,message:"请选择性别"}]},{default:l(()=>[e(J,{value:n.gender,"onUpdate:value":a[4]||(a[4]=t=>n.gender=t),options:te},null,8,["value","options"])]),_:1})]),_:1}),e(o,{span:8},{default:l(()=>[e(s,{name:"phone",label:"联系方式",rules:[{required:!0,message:"请输入联系方式"}]},{default:l(()=>[e(i,{value:n.phone,"onUpdate:value":a[5]||(a[5]=t=>n.phone=t),valueModifiers:{trim:!0}},null,8,["value"])]),_:1})]),_:1})]),_:1}),e(d,{gutter:24},{default:l(()=>[e(o,{span:24},{default:l(()=>[e(s,{name:"private_placement_strategy",label:"策略类型"},{default:l(()=>[e(S,{value:m.value,"onUpdate:value":a[7]||(a[7]=t=>m.value=t)},{default:l(()=>[(v(!0),w(C,null,Y(de,(t,h)=>(v(),x(q,{key:h,value:t.value},{default:l(()=>[p(O(t.label),1)]),_:2},1032,["value"]))),128)),L(e(i,{style:{width:"200px"},value:E.value,"onUpdate:value":a[6]||(a[6]=t=>E.value=t),valueModifiers:{trim:!0}},null,8,["value"]),[[z,m.value&&m.value.includes("other")]])]),_:1},8,["value"])]),_:1})]),_:1})]),_:1}),e(d,{gutter:24},{default:l(()=>[e(o,{span:24},{default:l(()=>[e(s,{name:"fund_demand",label:"资金需求"},{default:l(()=>[e(S,{value:c.value,"onUpdate:value":a[9]||(a[9]=t=>c.value=t)},{default:l(()=>[(v(!0),w(C,null,Y(ve,(t,h)=>(v(),x(q,{key:h,value:t.value},{default:l(()=>[p(O(t.label),1)]),_:2},1032,["value"]))),128)),L(e(i,{style:{width:"200px"},value:j.value,"onUpdate:value":a[8]||(a[8]=t=>j.value=t),valueModifiers:{trim:!0}},null,8,["value"]),[[z,c.value&&c.value.includes("other")]])]),_:1},8,["value"])]),_:1})]),_:1})]),_:1}),e(d,{gutter:24},{default:l(()=>[e(o,{span:24},{default:l(()=>[e(s,{name:"technical_demand",label:"技术需求"},{default:l(()=>[e(S,{value:k.value,"onUpdate:value":a[10]||(a[10]=t=>k.value=t)},{default:l(()=>[(v(!0),w(C,null,Y(pe,(t,h)=>(v(),x(q,{key:h,value:t.value},{default:l(()=>[p(O(t.label),1)]),_:2},1032,["value"]))),128))]),_:1},8,["value"])]),_:1})]),_:1})]),_:1}),e(d,{gutter:24},{default:l(()=>[e(o,{span:24},{default:l(()=>[e(s,{name:"bond_source_demand",label:"劵源需求"},{default:l(()=>[e(S,{value:b.value,"onUpdate:value":a[12]||(a[12]=t=>b.value=t)},{default:l(()=>[(v(!0),w(C,null,Y(fe,(t,h)=>(v(),x(q,{key:h,value:t.value},{default:l(()=>[p(O(t.label),1)]),_:2},1032,["value"]))),128)),L(e(i,{style:{width:"200px"},value:D.value,"onUpdate:value":a[11]||(a[11]=t=>D.value=t),valueModifiers:{trim:!0}},null,8,["value"]),[[z,b.value&&b.value.includes("other")]])]),_:1},8,["value"])]),_:1})]),_:1})]),_:1}),e(d,{gutter:24},{default:l(()=>[e(o,{span:24},{default:l(()=>[e(s,{name:"investment_research_demand",label:"投研需求"},{default:l(()=>[e(S,{value:g.value,"onUpdate:value":a[14]||(a[14]=t=>g.value=t)},{default:l(()=>[(v(!0),w(C,null,Y(me,(t,h)=>(v(),x(q,{key:h,value:t.value},{default:l(()=>[p(O(t.label),1)]),_:2},1032,["value"]))),128)),L(e(i,{style:{width:"200px"},value:R.value,"onUpdate:value":a[13]||(a[13]=t=>R.value=t),valueModifiers:{trim:!0}},null,8,["value"]),[[z,g.value&&g.value.includes("other")]])]),_:1},8,["value"])]),_:1})]),_:1})]),_:1}),e(d,{gutter:24},{default:l(()=>[e(o,{span:8},{default:l(()=>[e(s,{name:"existing_assets",label:"现有资产"},{default:l(()=>[e(i,{value:n.existing_assets,"onUpdate:value":a[15]||(a[15]=t=>n.existing_assets=t),valueModifiers:{trim:!0}},null,8,["value"])]),_:1})]),_:1}),e(o,{span:8},{default:l(()=>[e(s,{name:"historical_peak",label:"历史峰值"},{default:l(()=>[e(i,{value:n.historical_peak,"onUpdate:value":a[16]||(a[16]=t=>n.historical_peak=t),valueModifiers:{trim:!0}},null,8,["value"])]),_:1})]),_:1})]),_:1}),e(d,{gutter:24},{default:l(()=>[e(o,{span:8},{default:l(()=>[e(s,{name:"customer_source",label:"客户来源"},{default:l(()=>[e(i,{value:n.customer_source,"onUpdate:value":a[17]||(a[17]=t=>n.customer_source=t),valueModifiers:{trim:!0}},null,8,["value"])]),_:1})]),_:1}),e(o,{span:8},{default:l(()=>[e(s,{name:"specific_channel",label:"具体渠道"},{default:l(()=>[e(i,{value:n.specific_channel,"onUpdate:value":a[18]||(a[18]=t=>n.specific_channel=t),valueModifiers:{trim:!0}},null,8,["value"])]),_:1})]),_:1}),e(o,{span:8},{default:l(()=>[e(s,{name:"commission_rate",label:"佣金费率"},{default:l(()=>[e(i,{value:n.commission_rate,"onUpdate:value":a[19]||(a[19]=t=>n.commission_rate=t),valueModifiers:{trim:!0}},null,8,["value"])]),_:1})]),_:1})]),_:1}),e(d,{gutter:24},{default:l(()=>[e(o,{span:12},{default:l(()=>[e(s,{name:"risk_appetite",label:"风险偏好"},{default:l(()=>[e(J,{value:n.risk_appetite,"onUpdate:value":a[20]||(a[20]=t=>n.risk_appetite=t),options:ce},null,8,["value","options"])]),_:1})]),_:1}),e(o,{span:12},{default:l(()=>[e(s,{name:"permissions",label:"权限情况"},{default:l(()=>[e(S,{value:y.value,"onUpdate:value":a[21]||(a[21]=t=>y.value=t),options:ge},null,8,["value","options"])]),_:1})]),_:1})]),_:1}),F.value!=="add"?(v(),x(d,{key:0,gutter:24},{default:l(()=>[e(o,{span:6},{default:l(()=>[e(s,{label:"拜访情况"},{default:l(()=>[e(B,{href:"#",type:"link",onClick:Q(ue,["prevent"])},{default:l(()=>[p("详情")]),_:1},8,["onClick"])]),_:1})]),_:1}),e(o,{span:6},{default:l(()=>[e(s,{label:"已合作券商"},{default:l(()=>[e(B,{href:"#",type:"link",onClick:Q(ie,["prevent"])},{default:l(()=>[p("详情")]),_:1},8,["onClick"])]),_:1})]),_:1}),e(o,{span:6},{default:l(()=>[e(s,{label:"基金理财/私募"},{default:l(()=>[e(B,{type:"link",onClick:Q(se,["prevent"])},{default:l(()=>[p("详情")]),_:1},8,["onClick"])]),_:1})]),_:1})]),_:1})):na("",!0),_a,e(d,{gutter:24},{default:l(()=>[e(o,{span:12},{default:l(()=>[e(s,{name:"developer",label:" 开发关系"},{default:l(()=>[e(i,{value:n.developer,"onUpdate:value":a[22]||(a[22]=t=>n.developer=t),valueModifiers:{trim:!0}},null,8,["value"])]),_:1})]),_:1}),e(o,{span:12},{default:l(()=>[e(s,{name:"is_internet_channel",label:"是否是互联网渠道"},{default:l(()=>[e(J,{value:n.is_internet_channel,"onUpdate:value":a[23]||(a[23]=t=>n.is_internet_channel=t),options:be},null,8,["value","options"])]),_:1})]),_:1})]),_:1}),e(d,{gutter:24},{default:l(()=>[e(o,{span:12},{default:l(()=>[e(s,{name:"assignmenter",label:"服务包分配"},{default:l(()=>[e(i,{value:n.assignmenter,"onUpdate:value":a[24]||(a[24]=t=>n.assignmenter=t),valueModifiers:{trim:!0}},null,8,["value"])]),_:1})]),_:1}),e(o,{span:12},{default:l(()=>[e(s,{name:"follower",label:"跟进情况"},{default:l(()=>[e(i,{value:n.follower,"onUpdate:value":a[25]||(a[25]=t=>n.follower=t),valueModifiers:{trim:!0}},null,8,["value"])]),_:1})]),_:1})]),_:1}),da,e(d,{gutter:24},{default:l(()=>[e(o,{span:8},{default:l(()=>[e(s,{name:"account_opening_date",label:"开户日期"},{default:l(()=>[e(Se,{value:n.account_opening_date,"onUpdate:value":a[26]||(a[26]=t=>n.account_opening_date=t),placeholder:"YYYY-MM-DD","value-format":"YYYY-MM-DD",style:{width:"100%"}},null,8,["value"])]),_:1})]),_:1}),e(o,{span:8},{default:l(()=>[e(s,{name:"preferential_interest_rate",label:"优惠利率"},{default:l(()=>[e(i,{value:n.preferential_interest_rate,"onUpdate:value":a[27]||(a[27]=t=>n.preferential_interest_rate=t),valueModifiers:{trim:!0}},null,8,["value"])]),_:1})]),_:1}),e(o,{span:8},{default:l(()=>[e(s,{label:"时  间"},{default:l(()=>[e(Ye,{value:M.value,"onUpdate:value":a[28]||(a[28]=t=>M.value=t),format:T},null,8,["value"])]),_:1})]),_:1})]),_:1}),e(d,{gutter:24},{default:l(()=>[e(o,{span:24},{default:l(()=>[e(s,{name:"remark",label:"备  注"},{default:l(()=>[e(Fe,{value:n.remark,"onUpdate:value":a[29]||(a[29]=t=>n.remark=t),"show-count":"",maxlength:100},null,8,["value"])]),_:1})]),_:1})]),_:1}),e(d,{gutter:24},{default:l(()=>[e(o,{span:24,style:{"text-align":"center"}},{default:l(()=>[e(B,{type:"primary","html-type":"submit"},{default:l(()=>[p("提交")]),_:1}),e(B,{style:{margin:"0 8px"},onClick:I},{default:l(()=>[p(" 重置")]),_:1})]),_:1})]),_:1})]),_:1},8,["model"])]),_:1},8,["spinning"]),e(Me,{ref_key:"contactRef",ref:P,"form-type":"jgkh",onCancel:X,onOk:oe},null,512),e(Ue,{ref_key:"fundsRef",ref:$,onCancel:Z,onOk:re},null,512),e(we,{ref_key:"cooperationsRef",ref:N,onCancel:G,onOk:_e},null,512)],64)}}};export{Fa as default};
