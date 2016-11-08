/*======================================================================*\
|| #################################################################### ||
|| # vBulletin 4.2.2
|| # ---------------------------------------------------------------- # ||
|| # Copyright �2000-2013 vBulletin Solutions Inc. All Rights Reserved. ||
|| # This file may not be redistributed in whole or significant part. # ||
|| # ---------------- VBULLETIN IS NOT FREE SOFTWARE ---------------- # ||
|| # http://www.vbulletin.com | http://www.vbulletin.com/license.html # ||
|| #################################################################### ||
\*======================================================================*/
function vB_Overlay(A,D,C,B){if(AJAX_Compatible&&(typeof vb_disable_ajax=="undefined"||vb_disable_ajax<2)){this.init(A,D,C,B)}}vB_Overlay.prototype.init=function(A,E,C,B){this.flasheractive=false;this.status=0;this.content=null;this.background=null;this.overlaybox=null;this.overlaybox_content=null;this.progressimage=null;this.progressimagesrc=null;this.events_enabled=false;this.savebutton=null;this.cancelbutton=null;this.action=null;this.cancelurl=null;this.finishedurl=null;this.caller=null;this.title=null;this.statusmessage=null;this.disablecontrols=A;this.ajax_req=null;this.loadcontent=(E!=null);this.load_action=E;this.load_caller=B;this.load_args=C;this.orig_width=null;this.orig_height=null;this.events={overlayloadsuccess:new YAHOO.util.CustomEvent("overlayloadsuccess"),overlaysave:new YAHOO.util.CustomEvent("overlaysave"),ajaxloadsuccess:new YAHOO.util.CustomEvent("ajaxloadsuccess")};var D=YAHOO.util.Dom.get("vb_overlay_background");if(!D){this.fetch_overlay_html()}};vB_Overlay.prototype.fetch_overlay_html=function(){if(this.check_status(0)&&!YAHOO.util.Connect.isCallInProgress(this.ajax_req)){this.set_status(2,"Load Overlay HTML");var A=((typeof (SESSIONURL)=="undefined"||SESSIONURL=="")?"":SESSIONURL)+"do=overlay&ajax=1"+(typeof (SECURITYTOKEN)!="undefined"?"&securitytoken="+SECURITYTOKEN:"")+(typeof (ADMINHASH)!="undefined"?"&adminhash="+ADMINHASH:"");this.ajax_req=YAHOO.util.Connect.asyncRequest("POST",fetch_ajax_url("ajax.php"),{success:this.show_ajax_response_overlay,failure:this.handle_ajax_error,timeout:vB_Default_Timeout,scope:this},A)}};vB_Overlay.prototype.show_ajax_response_overlay=function(E){if(!this.check_status(2)){return }if(E.responseXML){var B=E.responseXML.getElementsByTagName("error");if(B.length){this.set_status(0,"display - error");alert(B[0].firstChild.nodeValue)}else{document.body.appendChild(string_to_node(E.responseXML.getElementsByTagName("html")[0].firstChild.nodeValue));var C=YAHOO.util.Dom.get("vb_overlay_background");this.background=document.body.appendChild(C);var A=YAHOO.util.Dom.get("vb_overlay_clearbackground");this.clearbackground=document.body.appendChild(A);var D=YAHOO.util.Dom.get("vb_overlay_overlaybox");if(is_moz){YAHOO.util.Dom.setStyle(D,"position","fixed")}this.overlaybox=document.body.appendChild(D);this.overlaybox_content=YAHOO.util.Dom.get("vb_overlay_overlaybox_content");this.savebox=YAHOO.util.Dom.get("vb_overlay_savebox");var F=YAHOO.util.Dom.get("vb_overlay_progressimage");this.progressimage=document.body.appendChild(F);this.progressimage.src=IMGDIR_MISC+"/lightbox_progress.gif";this.savebutton=YAHOO.util.Dom.get("vb_overlay_save");this.cancelbutton=YAHOO.util.Dom.get("vb_overlay_cancel");if(!this.disablecontrols){YAHOO.util.Event.on(this.savebutton,"click",this.save,this,true);YAHOO.util.Event.on(this.cancelbutton,"click",this.cancelform,this,true);YAHOO.util.Event.on(this.savebutton,"mouseover",this.flipbuttoncolor);YAHOO.util.Event.on(this.savebutton,"mouseout",this.flipbuttoncolor);YAHOO.util.Event.on(this.cancelbutton,"mouseover",this.flipbuttoncolor);YAHOO.util.Event.on(this.cancelbutton,"mouseout",this.flipbuttoncolor)}else{YAHOO.util.Dom.setStyle(this.savebutton,"display","none");YAHOO.util.Dom.setStyle(this.cancelbutton,"display","none")}this.closebutton=YAHOO.util.Dom.get("vb_overlay_close");YAHOO.util.Event.on(this.closebutton,"click",this.cancelform,this,true);YAHOO.util.Event.on(this.closebutton,"mouseover",this.flipbuttoncolor);YAHOO.util.Event.on(this.closebutton,"mouseout",this.flipbuttoncolor);this.title=YAHOO.util.Dom.get("vb_overlay_title");this.statusmessage=YAHOO.util.Dom.get("vb_overlay_status");this.events.overlayloadsuccess.fire();if(this.loadcontent){this.loadcontent=false;this.show_ajax(this.load_action,this.load_args,this.load_caller)}}}};vB_Overlay.prototype.show=function(){this.show_background(false);YAHOO.util.Dom.setStyle(this.savebox,"display","");this.show_overlaybox();if(!this.events_enabled){this.enable_events()}};vB_Overlay.prototype.close=function(){this.hideprogress();YAHOO.util.Dom.setStyle(this.background,"display","none");YAHOO.util.Dom.setStyle(this.overlaybox,"display","none");YAHOO.util.Dom.setStyle(this.savebox,"display","none");YAHOO.util.Dom.setStyle(this.overlaybox,"height","auto");YAHOO.util.Dom.setStyle(this.overlaybox,"width","auto");YAHOO.util.Dom.setStyle(this.overlaybox,"overflow","auto");if(this.events_enabled){this.disable_events()}this.set_status(0,"close")};vB_Overlay.prototype.show_html=function(B,C,A){if(this.check_status(0)){this.action=B;this.caller=A;this.show_background();if(this.content){this.content.parentNode.removeChild(this.content)}this.content=YAHOO.util.Dom.get(C);if(this.content){this.contentype="html";this.overlaybox_content.appendChild(this.content);YAHOO.util.Dom.setStyle(this.content,"display","");YAHOO.util.Dom.setStyle(this.savebox,"display","");this.show_overlaybox()}else{this.close()}}};vB_Overlay.prototype.show_ajax=function(C,B,A){if(arguments.length>3){noprogress=arguments[3]}else{noprogress=false}if(this.check_status(0)&&!YAHOO.util.Connect.isCallInProgress(this.ajax_req)){this.set_status(2,"Load Ajax Content");this.show_background(noprogress);this.action=C;this.caller=A;B+=((typeof (SESSIONURL)=="undefined"||SESSIONURL=="")?"":SESSIONURL)+"ajax=1"+(typeof (SECURITYTOKEN)!="undefined"?"&securitytoken="+SECURITYTOKEN:"")+(typeof (ADMINHASH)!="undefined"?"&adminhash="+ADMINHASH:"");this.ajax_req=YAHOO.util.Connect.asyncRequest("POST",fetch_ajax_url(this.action),{success:this.show_ajax_response_load,failure:this.handle_ajax_error,timeout:vB_Default_Timeout,scope:this},B)}};vB_Overlay.prototype.show_ajax_response_load=function(A){if(!this.check_status(2)){return }if(A.responseXML){this.orig_width=null;this.orig_height=null;this.parse_response(A.responseXML);this.events.ajaxloadsuccess.fire()}else{this.close()}};vB_Overlay.prototype.remove_scripts_from_element=function(E){if(E.getElementsByTagName==undefined){return""}var B,D,A=E.getElementsByTagName("SCRIPT");console.log(E.getElementsByTagName);console.log(B);var C={files:[],inline:[]};for(D=0;D<A.length;D++){B=A[D];if(B.src){C.files.push(B.src)}else{if(B.text){C.inline.push(B.text)}}}while(B=E.getElementsByTagName("script")[0]){B.parentNode.removeChild(B)}return C};vB_Overlay.prototype.run_inline_script=function(scripts,scope){if(!scripts){return }var runner=function(){try{for(var i=0;i<scripts.length;i++){eval(scripts[i])}}catch(exc){console.error("Exception running inline JS (%s): "+scripts[i],exc)}};runner.call(scope)};vB_Overlay.prototype.parse_response=function(E){this.events.overlaysave.unsubscribeAll();var H=E.getElementsByTagName("error");if(H.length){this.set_status(0,"handle_ajax_response - error");var K="";for(var C in H){if(null!=H[C].firstChild){K+=H[C].getAttribute("errcode")+": "+H[C].firstChild.nodeValue+"\n"}}alert(K)}var G=E.getElementsByTagName("url");if(G.length){for(var J=0;J<G.length;J++){switch(G[J].getAttribute("type")){case"cancel":this.cancelurl=G[J].firstChild.nodeValue;break;case"finished":this.finishedurl=G[J].firstChild.nodeValue;break}}}var I=E.getElementsByTagName("title");if(this.title!=undefined&&I.length){this.title.innerHTML=I[0].firstChild.nodeValue}var D=E.getElementsByTagName("html");var F=E.getElementsByTagName("status");if(F.length){var B=F[0].firstChild.nodeValue;this.set_status(3,"")}else{var B=0}var K=E.getElementsByTagName("message");if(B==2){if(K.length){this.hideprogress();this.flasher(K[0].firstChild.nodeValue,50,0.1)}this.close_on_finish();return }else{if(D.length&&(!this.content||B==1)){if(this.content){this.content.parentNode.removeChild(this.content)}this.overlaybox_content.innerHTML=E.getElementsByTagName("html")[0].firstChild.nodeValue;this.content=this.overlaybox_content.firstChild;while(this.content.nodeType!=1&&this.content.nextSibling){this.content=this.content.nextSibling}var A=this.remove_scripts_from_element(this.content);this.run_inline_script(A.inline,this);init_popupmenus(this.overlaybox_content);YAHOO.util.Dom.setStyle(this.content,"display","")}}if(this.content){YAHOO.util.Dom.setStyle(this.savebox,"display","");this.show_overlaybox();if(K.length){this.flasher(K[0].firstChild.nodeValue,50,0.1)}}else{this.close()}};vB_Overlay.prototype.close_on_finish=function(){if(this.flasheractive){thisC=this;setTimeout(function(){thisC.close_on_finish()},10)}else{if(this.finishedurl){window.location=this.finishedurl}else{this.close()}}};vB_Overlay.prototype.flasher=function(D,B,A){this.flasheractive=true;if(A==0.1){this.statusmessage.innerHTML=""}YAHOO.util.Dom.setStyle(this.statusmessage,"opacity",A);this.statusmessage.innerHTML=D;if(A<1){var C=this;setTimeout(function(){C.flasher(D,B,A+0.05)},B)}else{this.flasheractive=false}};vB_Overlay.prototype.slider=function(D,C,A){if(C>0){var E=D.length-C;this.statusmessage.innerHTML=D.substr(E);C++;if(C<=D.length){var B=this;setTimeout(function(){B.slider(D,C,A)},A)}}};vB_Overlay.prototype.show_background=function(A){var B=fetch_viewport_info();YAHOO.util.Dom.setStyle(this.background,"top","0px");YAHOO.util.Dom.setStyle(this.background,"display","");YAHOO.util.Dom.setStyle(this.background,"width",B.w+"px");YAHOO.util.Dom.setStyle(this.background,"height",B.h+"px");YAHOO.util.Dom.setXY(this.background,[B.x,B.y]);viewport_info=null;if(!A){this.showprogress()}if(!this.events_enabled){this.enable_events()}};vB_Overlay.prototype.show_overlaybox=function(C){this.set_status(3,"display - overlaybox");YAHOO.util.Dom.setStyle(this.overlaybox,"display","");var D=fetch_viewport_info();var B=false;var A=false;if(!YAHOO.util.Dom.hasClass(this.overlaybox,this.INSTANCE_ID)){YAHOO.util.Dom.addClass(this.INSTANCE_ID);B=true}if(this.orig_width==null){this.orig_width=this.overlaybox.offsetWidth;this.orig_height=this.overlaybox.offsetHeight}if(D.w-50>this.orig_width){YAHOO.util.Dom.setStyle(this.overlaybox,"width","auto")}else{YAHOO.util.Dom.setStyle(this.overlaybox,"width",((D.w-50)+"px"));YAHOO.util.Dom.setStyle(this.overlaybox,"overflow","auto");A=true}if(D.h-50>this.orig_height){YAHOO.util.Dom.setStyle(this.overlaybox,"height","auto")}else{YAHOO.util.Dom.setStyle(this.overlaybox,"height",((D.h-50)+"px"));YAHOO.util.Dom.setStyle(this.overlaybox,"overflow","auto")}if((D.w-50)>this.overlaybox.offsetWidth&&(D.h-50)>this.overlaybox.offsetHeight){YAHOO.util.Dom.setStyle(this.overlaybox,"overflow","visible")}center_element(this.overlaybox,null,A);viewport_info=null;if(!C){this.hideprogress()}};vB_Overlay.prototype.save=function(A){if(this.check_status(3)&&this.action&&YAHOO.util.Dom.getStyle(this.progressimage,"display")=="none"&&!this.flasheractive){this.showprogress();psuedoform=new vB_Hidden_Form(this.action);psuedoform.add_variable("ajax",1);if(typeof (SECURITYTOKEN)!="undefined"){psuedoform.add_variable("securitytoken",SECURITYTOKEN)}if(typeof (ADMINHASH)!="undefined"){psuedoform.add_variable("adminhash",ADMINHASH)}psuedoform.add_variables_from_object(this.overlaybox);this.events.overlaysave.fire(psuedoform);this.set_status(2,"Save Data");this.ajax_req=YAHOO.util.Connect.asyncRequest("POST",fetch_ajax_url(this.action),{success:this.handle_ajax_response_save,failure:this.handle_ajax_error,timeout:vB_Default_Timeout,scope:this},psuedoform.build_query_string())}};vB_Overlay.prototype.handle_ajax_response_save=function(A){this.hideprogress();if(!this.check_status(2)){return }if(A.responseXML){this.parse_response(A.responseXML)}};vB_Overlay.prototype.enable_events=function(){if(!this.events_enabled){YAHOO.util.Event.on(window,"resize",(is_ie?this.handle_viewport_change_ie:this.handle_viewport_change),this,true);YAHOO.util.Event.on(window,"scroll",(is_ie?this.handle_viewport_change_ie:this.handle_viewport_change),this,true);YAHOO.util.Event.on(window,"keydown",this.cancelform,this,true);this.events_enabled=true}};vB_Overlay.prototype.disable_events=function(){if(this.events_enabled){YAHOO.util.Event.removeListener(window,"resize",(is_ie?this.handle_viewport_change_ie:this.handle_viewport_change));YAHOO.util.Event.removeListener(window,"scroll",(is_ie?this.handle_viewport_change_ie:this.handle_viewport_change));this.events_enabled=false}};vB_Overlay.prototype.handle_viewport_change=function(){this.show_background(1);this.show_overlaybox(1)};vB_Overlay.prototype.handle_viewport_change_ie=function(){var A=this;setTimeout(function(){A.handle_viewport_change()},100)};vB_Overlay.prototype.check_status=function(A){if(this.status>=A){return true}else{console.warn("Checked status for %d, found %d",A,this.status);return false}};vB_Overlay.prototype.set_status=function(A,B){console.log("vB_Overlay :: Set status = %d (%s)",A,B);this.status=A};vB_Overlay.prototype.showprogress=function(B){YAHOO.util.Dom.setStyle(this.clearbackground,"display","");if(typeof (B)=="undefined"){B=""}var A=this["progressimage"+B];YAHOO.util.Dom.setStyle(A,"display","");if(!B){center_element(A)}};vB_Overlay.prototype.hideprogress=function(){YAHOO.util.Dom.setStyle(this.progressimage,"display","none");YAHOO.util.Dom.setStyle(this.clearbackground,"display","none")};vB_Overlay.prototype.flipbuttoncolor=function(A){var B=YAHOO.util.Dom.hasClass(this,"vb_overlay_highlight");if(B){YAHOO.util.Dom.removeClass(this,"vb_overlay_highlight")}else{YAHOO.util.Dom.addClass(this,"vb_overlay_highlight")}};vB_Overlay.prototype.cancelform=function(A){if((A&&A.type=="keydown"&&A.keyCode!=27)||YAHOO.util.Dom.getStyle(this.progressimage,"display")==""||this.flasheractive){return }if(this.cancelurl){window.location=this.cancelurl}else{this.close()}};vB_Overlay.prototype.handle_ajax_error=function(A){this.close();vBulletin_AJAX_Error_Handler(A)};