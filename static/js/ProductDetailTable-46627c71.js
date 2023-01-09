import{m as u,D as q,I as A,u as V,w as J,k as Q,e as K}from"./ant-design-vue-a65eb274.js";import{_ as G,a as y}from"./index-4cbe4d0c.js";import{c as H}from"./lodash-es-26de6f87.js";import{e as W,l as b,r as X,aL as c,al as C,b8 as $,an as m,F as Z,E as T,ac as ee,c as U,ao as E,am as te,aN as ae,aM as ne}from"./@vue-e16f66a9.js";function de(){return"xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g,function(r){var D=Math.random()*16|0,p=r==="x"?D:D&3|8;return p.toString()})}const oe=r=>(ae("data-v-0ea8d16a"),r=r(),ne(),r),ie={key:0},le={key:1,class:"editable-row-operations"},se={key:0},ce={key:1},ue=["onClick"],_e=oe(()=>E("a",{style:{color:"#f0515f"}},"删除",-1)),re={__name:"ContactDetailTable",props:{formType:{type:String,default:"grkh"},isReadOnly:{type:Boolean,default:!1},customerId:{type:[String,Number]}},setup(r,{expose:D}){const p=r,h=W("$http"),v="YYYY-MM-DD",I=[{title:p.formType==="jgkh"?"拜访日期":"联系日期",dataIndex:"contact_date"},{title:p.formType==="jgkh"?"拜访情况说明":"联系情况说明",dataIndex:"contact_detail"},{title:"需求",dataIndex:"demand"},{title:p.formType==="jgkh"?"预约下次拜访时间":"预约下次联系时间",dataIndex:"next_contact_date"},{title:"提醒时长",dataIndex:"remind_duration"},{title:"操作",dataIndex:"operation",fixed:"right",width:"160px"}];p.isReadOnly&&I.splice(I.length-1,1);const _=b([]),w=b(!1),t=X({}),f=b([]),i=b({current:1,pageSize:10,total:0,showQuickJumper:!0,showSizeChanger:!0,showTotal:e=>`共${e}条`}),z=e=>{i.value.current=e.current,i.value.pageSize=e.pageSize,i.value.total=e.total,x()},F=()=>{const e={id:de(),customer_id:p.customerId,contact_date:"",contact_detail:"",demand:"",next_contact_date:"",remind_duration:""};_.value.unshift(e),f.value.push(e.id),S(e.id),i.value.current=1},x=(e=null)=>{w.value=!0,e!==null&&(i.value.current=1);const a={customerId:p.customerId,pageNo:i.value.current,pageSize:i.value.pageSize};h.get(y.contacts,{params:a}).then(d=>{const{data:l,total:k}=d;_.value=l,i.value.total=k}).finally(()=>{w.value=!1})},S=e=>{t[e]=H(_.value.filter(a=>e===a.id)[0])},M=e=>{const a=["contact_date","contact_detail","demand","next_contact_date","remind_duration"];let d=!0;return a.forEach(l=>{t[e][l]===""&&(d=!1)}),d},L=e=>{if(!M(e)){u.warning("请完整填写表格");return}f.value.includes(e)?Y(e):B(e)},Y=e=>{const a=u.loading("正在提交",0);h.post(y.contacts,{...t[e]}).then(d=>{d.code===0&&(u.success("新增成功"),x(1),f.value=f.value.filter(l=>l.id!==e))}).finally(()=>{g(e),a()})},B=e=>{const a=u.loading("正在提交",0);h.put(`${y.contacts}/${e}`,{...t[e]}).then(d=>{d.code===0&&(u.success("编辑成功"),x(1))}).finally(()=>{g(e),a()})},g=e=>{delete t[e]},N=e=>{if(f.value.includes(e))_.value=_.value.filter(a=>a.id!==e),u.success("删除成功");else{const a=u.loading("正在删除",0);h.delete(`${y.contacts}/${e}`).then(d=>{d.code===0&&(u.success("删除成功"),_.value=_.value.filter(l=>l.id!==e),x(1))}).finally(()=>{a()})}};return D({dataSource:_,columns:I,editableData:t,paginationOptions:i,dateFormat:v,edit:S,save:L,cancel:g,deleteRecord:N,handleAdd:F,handleTableChange:z,submitAdd:Y,submitEdit:B,fetchTableData:x}),(e,a)=>{const d=q,l=A,k=V,R=J,O=Q,P=K;return c(),C(P,{columns:I,loading:w.value,"data-source":_.value,pagination:i.value,onChange:z,scroll:{x:1500},bordered:"","row-key":"id"},{bodyCell:$(({column:o,text:j,record:n})=>[["contact_date","contact_detail","demand","next_contact_date","remind_duration"].includes(o.dataIndex)?(c(),m("div",ie,[["contact_date","next_contact_date"].includes(o.dataIndex)&&t[n.id]?(c(),C(d,{key:0,value:t[n.id][o.dataIndex],"onUpdate:value":s=>t[n.id][o.dataIndex]=s,"value-format":v},null,8,["value","onUpdate:value"])):["contact_detail","demand"].includes(o.dataIndex)&&t[n.id]?(c(),C(l,{key:1,value:t[n.id][o.dataIndex],"onUpdate:value":s=>t[n.id][o.dataIndex]=s,style:{margin:"-5px 0"}},null,8,["value","onUpdate:value"])):o.dataIndex==="remind_duration"&&t[n.id]?(c(),C(k,{key:2,value:t[n.id][o.dataIndex],"onUpdate:value":s=>t[n.id][o.dataIndex]=s},null,8,["value","onUpdate:value"])):(c(),m(Z,{key:3},[T(ee(j),1)],64))])):o.dataIndex==="operation"?(c(),m("div",le,[t[n.id]?(c(),m("span",se,[U(R,{onClick:s=>L(n.id)},{default:$(()=>[T("保存")]),_:2},1032,["onClick"]),U(R,{onClick:s=>g(n.id)},{default:$(()=>[T("取消")]),_:2},1032,["onClick"])])):(c(),m("span",ce,[E("a",{onClick:s=>S(n.id)},"编辑",8,ue),U(O,{title:"确定删除该条记录吗?",onConfirm:s=>N(n.id)},{default:$(()=>[_e]),_:2},1032,["onConfirm"])]))])):te("",!0)]),_:1},8,["loading","data-source","pagination"])}}},Se=G(re,[["__scopeId","data-v-0ea8d16a"]]);const pe=r=>(ae("data-v-eec47142"),r=r(),ne(),r),ve={key:0},fe={key:1,class:"editable-row-operations"},xe={key:0},me={key:1},he=["onClick"],ge=pe(()=>E("a",{style:{color:"#f0515f"}},"删除",-1)),Ie={__name:"ProductDetailTable",props:{isReadOnly:{type:Boolean,default:!1},customerId:{type:[String,Number]}},setup(r,{expose:D}){const p=r,h=[{title:"购买产品",dataIndex:"name"},{title:"购买金额",dataIndex:"amount"},{title:"收益率情况",dataIndex:"yield_rate"},{title:"购买时间",dataIndex:"buy_date"},{title:"产品天数",dataIndex:"day_number"},{title:"到期时间",dataIndex:"due_date"},{title:"操作",dataIndex:"operation",fixed:"right",width:"160px"}];p.isReadOnly&&h.splice(h.length-1,1);const v=b([]),I=b(!1),_=W("$http"),w="YYYY-MM-DD",t=X({}),f=b([]),i=b({current:1,pageSize:10,total:0,showQuickJumper:!0,showSizeChanger:!0,showTotal:e=>`共${e}条`}),z=e=>{i.value.current=e.current,i.value.pageSize=e.pageSize,i.value.total=e.total,x()},F=()=>{const e={id:de(),customer_id:p.customerId,buy_date:"",name:"",amount:"",yield_rate:"",due_date:"",day_number:""};v.value.unshift(e),f.value.push(e.id),S(e.id),i.value.current=1},x=(e=null)=>{I.value=!0,e!==null&&(i.value.current=1);const a={customerId:p.customerId,pageNo:i.value.current,pageSize:i.value.pageSize};_.get(y.funds,{params:a}).then(d=>{const{data:l,total:k}=d;v.value=l,i.value.total=k}).finally(()=>{I.value=!1})},S=e=>{t[e]=H(v.value.filter(a=>e===a.id)[0])},M=e=>{const a=["name","amount","yield_rate","buy_date","day_number","due_date"];let d=!0;return a.forEach(l=>{t[e][l]===""&&(d=!1)}),d},L=e=>{if(!M(e)){u.warning("请完整填写表格");return}f.value.includes(e)?Y(e):B(e)},Y=e=>{const a=u.loading("正在提交",0);_.post(y.funds,{...t[e]}).then(d=>{d.code===0&&(u.success("新增成功"),x(1),f.value=f.value.filter(l=>l.id!==e))}).finally(()=>{g(e),a()})},B=e=>{const a=u.loading("正在提交",0);_.put(`${y.funds}/${e}`,{...t[e]}).then(d=>{d.code===0&&(u.success("编辑成功"),x(1))}).finally(()=>{g(e),a()})},g=e=>{delete t[e]},N=e=>{if(f.value.includes(e))v.value=v.value.filter(a=>a.id!==e),u.success("删除成功");else{const a=u.loading("正在删除",0);_.delete(`${y.funds}/${e}`).then(d=>{d.code===0&&(u.success("删除成功"),v.value=v.value.filter(l=>l.id!==e),x(1))}).finally(()=>{a()})}};return D({dataSource:v,columns:h,dateFormat:w,editingKey:"",editableData:t,paginationOptions:i,edit:S,save:L,cancel:g,deleteRecord:N,handleAdd:F,handleTableChange:z,fetchTableData:x}),(e,a)=>{const d=q,l=A,k=V,R=J,O=Q,P=K;return c(),C(P,{columns:h,loading:I.value,"data-source":v.value,pagination:i.value,onChange:z,bordered:""},{bodyCell:$(({column:o,text:j,record:n})=>[["name","amount","yield_rate","buy_date","day_number","due_date"].includes(o.dataIndex)?(c(),m("div",ve,[["buy_date","due_date"].includes(o.dataIndex)&&t[n.id]?(c(),C(d,{key:0,value:t[n.id][o.dataIndex],"onUpdate:value":s=>t[n.id][o.dataIndex]=s,"value-format":w},null,8,["value","onUpdate:value"])):o.dataIndex==="name"&&t[n.id]?(c(),C(l,{key:1,value:t[n.id][o.dataIndex],"onUpdate:value":s=>t[n.id][o.dataIndex]=s,style:{margin:"-5px 0"}},null,8,["value","onUpdate:value"])):["amount","yield_rate","day_number"].includes(o.dataIndex)&&t[n.id]?(c(),C(k,{key:2,value:t[n.id][o.dataIndex],"onUpdate:value":s=>t[n.id][o.dataIndex]=s},null,8,["value","onUpdate:value"])):(c(),m(Z,{key:3},[T(ee(j),1)],64))])):o.dataIndex==="operation"?(c(),m("div",fe,[t[n.id]?(c(),m("span",xe,[U(R,{onClick:s=>L(n.id)},{default:$(()=>[T("保存")]),_:2},1032,["onClick"]),U(R,{onClick:s=>g(n.id)},{default:$(()=>[T("取消")]),_:2},1032,["onClick"])])):(c(),m("span",me,[E("a",{onClick:s=>S(n.id)},"编辑",8,he),U(O,{title:"确定删除该条记录吗?",onConfirm:s=>N(n.id)},{default:$(()=>[ge]),_:2},1032,["onConfirm"])]))])):te("",!0)]),_:1},8,["loading","data-source","pagination"])}}},ke=G(Ie,[["__scopeId","data-v-eec47142"]]);export{Se as C,ke as P,de as u};
