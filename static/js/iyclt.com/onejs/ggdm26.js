// JavaScript Document
function addLoadEvent(func) {
  var oldonload = window.onload;
  if (typeof window.onload != 'function') {
	window.onload = func;
	}else{
	window.onload = function() {
    oldonload();
    func();
    }
  }
}

function addClass(element,value) {
  if (!element.className) {
    element.className = value;
  } else {
    newClassName = element.className;
    newClassName+= " ";
    newClassName+= value;
    element.className = newClassName;
  }
}

function removeClass(element, value){
  var removedClass = element.className;
  var pattern = new RegExp("(^| )" + value + "( |$)");
  removedClass = removedClass.replace(pattern, "$1");
  removedClass = removedClass.replace(/ $/, "");
  element.className = removedClass;
  return true;
}

/*className */
function getElementsByClass(searchClass,node,tag) {
 var classElements = new Array();
 if ( node == null )
  node = document;
 if ( tag == null )
  tag = '*';
 var els = node.getElementsByTagName(tag);
 var elsLen = els.length;
 var pattern = new RegExp("(^|\\s)"+searchClass+"(\\s|$)");
 for (var i = 0, j = 0; i < elsLen; i++) {
  if ( pattern.test(els[i].className) ) {
   classElements[j] = els[i];
   j++;
  }
 }
 return classElements;
}


/*break ul tag*/
function breakul(ul_ID,li_num){
		if (!document.getElementById(ul_ID)) return false;
		var divid = document.getElementById(ul_ID).parentNode; 
		var sfEls = divid.getElementsByTagName("li"); 
		var loopCount = Math.ceil(sfEls.length/li_num) - 1; 
		for(var less = 0;less<loopCount;less++) {
			var bod = document.createElement("ul");  
			divid.appendChild(bod);
			for(var i = 0;i<li_num;i++) {
					   if(sfEls[li_num] && ((less+1)*li_num +i)<sfEls.length){
					   bod.appendChild(sfEls[li_num]);
			}  
		}   
	}
}

function all_func(){
	breakul('break_hangqing',6);
	breakul('break_weihu',6);
	breakul('break_shangjia',5);
	breakul('break_redian',8);
	tabs("car_tab_ul","data_table","best_car",true);
	tabs("car_tab_ul2","data_table2","best_car2",true);
	tabs("car_tab_ul3","data_table3",null,true);
	tabs("sub_ul","sub_con",null,true);
	tabs("sub_news","sub_news_con",null,true);	
	tabs("rank_newcar_tab","rank_newcar");
	tabs("pageTop","ctab");
	tabs("link_tab_ul","link_box",null,true);
	var focusa = new focusObj('focus_chart',3000);

}
addLoadEvent(all_func)
	
/*==================focus=====================*/

/*imgchange*/
function focusbigimg(obj,focus_obj){	
	var focus_box = focus_obj;
	var divs = focus_box.getElementsByTagName("div");
	var ps = focus_box.getElementsByTagName("p");
	
	for(var i=0;i<ps.length;i++){
		if (divs[i]==obj){ps[i].style.display = "block";}
		else{ps[i].style.display = "none";}
	}
	
}

/*wdith*/
function widthElement(elementID,final_width,interval) {
  
  if(typeof(elementID)=='object'&&typeof(elementID.tagName)!='undefined'){
	  var elem = elementID;
	}else if(typeof(elementID)=='string'){
		var elem = document.getElementById(elementID);
	}else if(!document.getElementById(elementID)){
		return false;  
	}

  if (elem.movement) {
   clearTimeout(elem.movement); 
  }
  if (!elem.style.width) {
    elem.style.width = "0px";
  }
  var xpos = parseInt(elem.style.width);
  if (xpos == final_width) {
	 return true;	
  }  
  if (xpos < final_width) {
    var dist = Math.ceil((final_width - xpos)/3);
    xpos = xpos + dist;
  }
  if (xpos > final_width) {
    var dist = Math.ceil((xpos - final_width)/3);
    xpos = xpos - dist;
  }
  elem.style.width = xpos + "px";
  var repeat = "widthElement('"+elementID+"',"+final_width+","+interval+")";
  elem.movement = setTimeout(repeat,interval);
}

getcurrent=0;	

/*auto*/
function focusAuto(bt_autokey,focus_box,bt_max_width,bt_min_width,bt_interval){
	
	if(bt_autokey) {return false;}//key
	if(!focus_box) {return false;}
	var f_div = focus_box.getElementsByTagName("div");

	var getc = getElementsByClass("current",focus_box,"div");
	li_active();
					
	var getc = getElementsByClass("current",focus_box,"div");	
	focusbigimg(getc[0],focus_box);	
	
	function li_active(){
		if(f_div[f_div.length-1].className == "current" && f_div[f_div.length-1].style.width == bt_max_width+"px" ){
					removeClass(f_div[f_div.length-1], "current");		
					addClass(f_div[0],"current")	
					widthElement(f_div[f_div.length-1].id,bt_min_width,bt_interval);
					widthElement(f_div[0].id,bt_max_width,bt_interval);
					return false;
				}
			if(getc[0].style.width == bt_max_width+"px"){					
					for(var i=0;i<f_div.length;i++){
						if(f_div[i] == getc[0]){
							var getcurrent = i;//sub key
						}					
					}					
					removeClass(f_div[getcurrent], "current");
					addClass(f_div[getcurrent+1],"current")
					widthElement(f_div[getcurrent].id,bt_min_width,bt_interval);
					widthElement(f_div[getcurrent+1].id,bt_max_width,bt_interval);
					getcurrent=getcurrent++;					
				}	
	}
}
//addLoadEvent(focusAuto);
function focusObj(id,settime){
//定义焦点模块对象属性
	if (!document.getElementById(id)) return false;
	this.focus_box = document.getElementById(id);
	this.f_p = this.focus_box.getElementsByTagName("p");
	this.f_em = this.focus_box.getElementsByTagName("em");
	this.f_div = this.focus_box.getElementsByTagName("div");
	this.getc = getElementsByClass("current",this.focus_box,"div");

	var w_max_width=parseInt(this.focus_box.clientWidth-this.f_div.length*18);//计算显示块宽度
	
	this.bt_autokey = false;
	this.bt_interval = 30;	
	this.bt_min_width = 18;
	this.bt_max_width = w_max_width+8;
	this.getc[0].style.width=w_max_width+8 + "px";//load width
	
//对象属性参数化 便于传参	
	var wbt_autokey=this.bt_autokey;
	var wfocus_box=this.focus_box;
	var wbt_max_width=this.bt_max_width;
	var wbt_min_width=this.bt_min_width;
	var wbt_interval=this.bt_interval;
	var wf_em=this.f_em;
	var wf_div=this.f_div;
	
	
	for(var i=0;i<this.f_em.length;i++){
		this.f_div[i].onmouseover = function(){wbt_autokey = true;};//key
		this.f_div[i].onmouseout = function(){wbt_autokey = false;};//key	
		this.f_p[i].onmouseover = function(){wbt_autokey = true;};//key
        this.f_p[i].onmouseout = function(){wbt_autokey = false;};//key  

		this.f_p[i].style.display = "none";
		this.f_p[0].style.display = "block";
		
		this.f_em[i].num = i;//em元素赋 num 属性
	
		this.f_em[i].onclick = function(){
			var getc = getElementsByClass("current",wfocus_box,"div");
			if(getc[0].style.width != wbt_max_width+"px"){return false};//unable quick click
			if(getc[0]==this.parentNode.parentNode){return false};//unable click current
			
			widthElement(getc[0].id,wbt_min_width,wbt_interval);
			widthElement(wf_div[this.num].id,wbt_max_width,wbt_interval);
			removeClass(getc[0],"current");
			addClass(wf_div[this.num],"current");
			focusbigimg(wf_div[this.num],wfocus_box);
			return false;
			
			}; 
		
	}
	this.bt_settime = setInterval(function(){focusAuto(wbt_autokey,wfocus_box,wbt_max_width,wbt_min_width,wbt_interval);},settime);
	

}


/*=======================tab=============================*/
function hide(id){var Div = document.getElementById(id);if(Div){Div.style.display="none"}}  
function show(id){var Div = document.getElementById(id);if(Div){Div.style.display="block"}}  

function tabsRemove(index,head,divs,div2s) { 		
	if (!document.getElementById(head)) return false;
	var tab_heads = document.getElementById(head);
	if (tab_heads) {
		var alis = tab_heads.getElementsByTagName("li");  
		for(var i=0;i<alis.length;i++){
			removeClass(alis[i], "current");
			
			hide(divs+"_"+i);
			if(div2s){hide(div2s+"_"+i)};
			
			if (i==index) {
				addClass(alis[i],"current");
			}
			}
			
			show(divs+"_"+index);
			if(div2s){show(div2s+"_"+index)};
		}
}

function tabs(head,divs,div2s,over){
	if (!document.getElementById(head)) return false;
	var tab_heads=document.getElementById(head);
	
	if (tab_heads) {
	   var alis=tab_heads.getElementsByTagName("li");
	   for(var i=0;i<alis.length;i++) {
		alis[i].num=i;
		
		
		if(over){
				alis[i].onmouseover = function(){
					var thisobj = this;
					thetabstime = setTimeout(function(){changetab(thisobj);},150);
					}
				alis[i].onmouseout = function(){
					clearTimeout(thetabstime);
					}			
		}
		else{			
					alis[i].onclick = function(){
						if(this.className == "current" || this.className == "last current"){
							changetab(this);
							return true;
						}
						else{
							changetab(this);						
							return false;
						}
					
				}
		}
		
		function changetab(thebox){
			tabsRemove(thebox.num,head,divs,div2s);			
		}
  
     } 
  }/*www.16sucai.com*/
}
