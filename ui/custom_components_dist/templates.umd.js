(function(e,l){typeof exports=="object"&&typeof module<"u"?module.exports=l(require("vue"),require("../injectionKeys.ts")):typeof define=="function"&&define.amd?define(["vue","../injectionKeys.ts"],l):(e=typeof globalThis<"u"?globalThis:e||self,e.StreamsyncCustomComponentTemplates=l(e.vue,e.injectionKeys))})(this,function(e,l){"use strict";var a=(t=>(t.Text="Text",t.KeyValue="Key-Value",t.Color="Color",t.Shadow="Shadow",t.Number="Number",t.Object="Object",t.IdKey="Identifying Key",t))(a||{}),s=(t=>(t.General="General",t.Style="Style",t))(s||{}),y=(t=>(t.Text="Text",t.Textarea="Textarea",t))(y||{});const u=t=>(e.pushScopeId("data-v-c47a5383"),t=t(),e.popScopeId(),t),_={class:"BubbleMessage"},g=u(()=>e.createElementVNode("div",{class:"triangle"},null,-1)),b={class:"message"},h={streamsync:{name:"Bubble Message",description:"Shows a message in the shape of a speech bubble.",category:"Content",fields:{text:{name:"Text",type:a.Text}},previewField:"text"}},f=e.defineComponent({...h,__name:"BubbleMessage",setup(t){const n=e.inject(l.evaluatedFields);return(o,c)=>(e.openBlock(),e.createElementBlock("div",_,[g,e.createElementVNode("div",b,e.toDisplayString(e.unref(n).text.value),1)]))}}),$="",m=(t,n)=>{const o=t.__vccOpts||t;for(const[c,p]of n)o[c]=p;return o},S=m(f,[["__scopeId","data-v-c47a5383"]]);a.Color,s.Style;const x={name:"Primary text",type:a.Color,category:s.Style,applyStyleVariable:!0};a.Color,s.Style,a.Color,s.Style;const C={name:"Container background",type:a.Color,category:s.Style,applyStyleVariable:!0};a.Shadow,s.Style;const v={name:"Separator",type:a.Color,category:s.Style,applyStyleVariable:!0};a.Color,s.Style,a.Color,s.Style,a.Shadow,s.Style,a.Color,s.Style;const E={name:"Custom CSS classes",type:a.Text,category:s.Style,desc:"CSS classes, separated by spaces. You can define classes in custom stylesheets."},d=t=>(e.pushScopeId("data-v-026368bf"),t=t(),e.popScopeId(),t),V=d(()=>e.createElementVNode("div",{class:"triangle"},null,-1)),B={class:"message"},w={class:"text"},k=[d(()=>e.createElementVNode("i",{class:"ri-pushpin-line"},null,-1))],M=[d(()=>e.createElementVNode("i",{class:"ri-flag-line"},null,-1))],T=`This documentation will show in the collapsible mini-docs feature embedded in Builder.
You _can_ use **markdown**.`,I=`
def handle_flag(state, payload):
	state["flagged_message_id"] = payload`,N=`
def handle_pin(state, payload):
	state["pinned_message_id"] = payload`,j={streamsync:{name:"Bubble Message (Advanced)",description:"Shows a message in the shape of a speech bubble.",docs:T,category:"Content",fields:{messageId:{name:"Message id",desc:"Unique id to identify the message when generating events.",init:"a1",type:a.Text},text:{name:"Text",desc:"The message to be displayed.",default:"(Empty message)",type:a.Text,control:y.Textarea},orientation:{name:"Orientation",category:s.Style,type:a.Text,options:{left:"Pointing left",right:"Pointing right"}},bubbleColor:{name:"Bubble",default:"#CFEFF3",category:s.Style,type:a.Color,applyStyleVariable:!0},primaryTextColor:x,separatorColor:v,containerBackgroundColor:C,cssClasses:E},events:{"pin-message":{desc:"Emitted when the pin button is clicked.",stub:N},"flag-message":{desc:"Emitted when the flag button is clicked.",stub:I}},previewField:"text"}},A=e.defineComponent({...j,__name:"BubbleMessageAdvanced",setup(t){const n=e.ref(null),o=e.inject(l.evaluatedFields),c=e.computed(()=>o.messageId.value);function p(){const r=c.value,i=new CustomEvent("flag-message",{detail:{payload:r}});n.value.dispatchEvent(i)}function K(){const r=c.value,i=new CustomEvent("pin-message",{detail:{payload:r}});n.value.dispatchEvent(i)}return(r,i)=>(e.openBlock(),e.createElementBlock("div",{class:e.normalizeClass(["BubbleMessage",{rightOriented:e.unref(o).orientation.value=="right"}]),ref_key:"rootEl",ref:n},[V,e.createElementVNode("div",B,[e.createElementVNode("div",w,e.toDisplayString(e.unref(o).text.value),1),e.createElementVNode("div",{class:"actions"},[e.createElementVNode("div",{class:"action",onClick:K},k),e.createElementVNode("div",{class:"action",onClick:p},M)])])],2))}}),D="";return{bubblemessage:S,bubblemessageadvanced:m(A,[["__scopeId","data-v-026368bf"]])}});
