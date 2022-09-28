/*
 * None message check
 */
$(document).ready(function(){
	for(i=0; i<$("input").length;i++){
		if($("input")[i].value == "None")
			$("input")[i].value = "";
	}
	for(i=0;i<$("td").length;i++){
		if($("td")[i].textContent == "None")
			$("td")[i].textContent = "";
	}
});

/*
 * AJAX 评分
 */
//Initialization
window.onload = function(){

	var oStar = document.getElementById("star");
	var aLi = oStar.getElementsByTagName("li");
	var oUl = oStar.getElementsByTagName("ul")[0];
	var oSpan = oStar.getElementsByTagName("span")[1];
	var oP = oStar.getElementsByTagName("p")[0];
	var i = iScore = iStar = 0;
	var aMsg = [
				"Too Bad|It's so bad!",
				"Not Satisfated|The quality is below my expectation！",
				"So So|Just so so. Nothing much.",
				"Satisfated|The movie is good!",
				"Excellent|Best movie ever!"
				]
	
	for (i = 1; i <= aLi.length; i++){
		aLi[i - 1].index = i;
		
		//鼠标移过显示分数
		aLi[i - 1].onmouseover = function (){
			fnPoint(this.index);
			//浮动层显示
			oP.style.display = "block";
			//计算浮动层位置
			oP.style.left = oUl.offsetLeft + this.index * this.offsetWidth - 104 + "px";
			//匹配浮动层文字内容
			oP.innerHTML = "<em><b>" + this.index + "</b> Point " + aMsg[this.index - 1].match(/(.+)\|/)[1] + "</em>" + aMsg[this.index - 1].match(/\|(.+)/)[1]
		};
		
		//鼠标离开后恢复上次评分
		aLi[i - 1].onmouseout = function (){
			fnPoint();
			//关闭浮动层
			oP.style.display = "none"
		};
		
		//点击后进行评分处理
		aLi[i - 1].onclick = function (){
			iStar = this.index;
			oP.style.display = "none";
			oSpan.innerHTML = "<strong>" + (this.index) + " Point</strong> (" + aMsg[this.index - 1].match(/\|(.+)/)[1] + ")"
		}
	}
	
	//评分处理
	function fnPoint(iArg){
		//分数赋值
		iScore = iArg || iStar;
		for (i = 0; i < aLi.length; i++) aLi[i].className = i < iScore ? "on" : "";	
	}
	
}

//评分  get
$(document).ready(function(){
	  $("#star").click(function(){
		  var url = location.protocol + '//' 
		  	+ location.host + "/rating/" + location.search + "&rate=" + iScore;  
		  $.get(url, function(data,status){
			  if(data == 'success!'){
				  alert("Response：" + data );
			  }
			  if(data == 'login!'){
				  alert("Response：" + data );
				  self.location.href = "/login/";
			  }
		  });
	  });
	});

/*
 * 分页
 */
function showPages(name) {
	this.name = name;      //对象名称
	this.page = 1;         //当前页数
	this.pageCount = 1;    //总页数
	this.argName = 'page'; //参数名
	this.showTimes = 1;    //打印次数
}

showPages.prototype.getPage = function(){ //丛url获得当前页数,如果变量重复只获取最后一个
	var args = location.search;
	var reg = new RegExp('[\?&]?' + this.argName + '=([^&]*)[&$]?', 'gi');
	var chk = args.match(reg);
	this.page = RegExp.$1;
}
showPages.prototype.checkPages = function(){ //进行当前页数和总页数的验证֤
	if (isNaN(parseInt(this.page))) this.page = 1;
	if (isNaN(parseInt(this.pageCount))) this.pageCount = 1;
	if (this.page < 1) this.page = 1;
	if (this.pageCount < 1) this.pageCount = 1;
	if (this.page > this.pageCount) this.page = this.pageCount;
	this.page = parseInt(this.page);
	this.pageCount = parseInt(this.pageCount);
}
showPages.prototype.createHtml = function(){ //生成html代码
	var strHtml = '', prevPage = this.page - 1, nextPage = this.page + 1;
	
	//strHtml += '<div class="page">';
	strHtml += '<div class="black">';
	<!-- Button Field -->
	
	if (prevPage < 1) {
		strHtml += '<span title="Prev Page" class="disabled">&lt;</span>';
	} else {
		strHtml += '<span title="Prev Page"><a href="javascript:' + this.name + '.toPage(' + prevPage + ');">&lt;</a></span>';
	}
	if (this.page != 1) strHtml += '<span title="Page 1"><a href="javascript:' + this.name + '.toPage(1);">1</a></span>';
	if (this.page >= 5) strHtml += '<span>...</span>';
	if (this.pageCount > this.page + 2) {
		var endPage = this.page + 2;
	} else {
		var endPage = this.pageCount;
	}
	for (var i = this.page - 2; i <= endPage; i++) {
		if (i > 0) {
			if (i == this.page) {
				strHtml += '<span class="current" title="Page ' + i + '">' + i + '</span>';
			} else {
				if (i != 1 && i != this.pageCount) {
					strHtml += '<span title="Page ' + i + '"><a href="javascript:' + this.name + '.toPage(' + i + ');">' + i + '</a></span>';
				}
			}
		}
	}
	if (this.page + 3 < this.pageCount) strHtml += '<span>...</span>';
	if (this.page != this.pageCount) strHtml += '<span title="Page ' + this.pageCount + '"><a href="javascript:' + this.name + '.toPage(' + this.pageCount + ');">' + this.pageCount + '</a></span>';
	if (nextPage > this.pageCount) {
		strHtml += '<span title="Next Page" class="disabled">&gt;</span>';
	} else {
		strHtml += '<span title="Next Page"><a href="javascript:' + this.name + '.toPage(' + nextPage + ');">&gt;</a></span>';
	}
	
	<!-- end Button Fields-->
	
	<!-- Input Box-->
	//Input Box
	strHtml += '<span class="input">';
	if (this.pageCount < 1) {
		strHtml += '<input type="text" name="toPage" value="No Pages" class="itext" disabled="disabled">';
		strHtml += '<input type="button" name="go" value="GO" class="ibutton" disabled="disabled"></option>';
	} else {
		strHtml += '<input type="text" id="pageInput' + this.showTimes + '" value="' + this.page + '" class="itext" title="Input page" onkeypress="return ' + this.name + '.formatInputPage(event);" onfocus="this.select()">';
		strHtml += '<input type="text" value=" / ' + this.pageCount + '" class="icount" readonly="readonly">';
		strHtml += '<input type="button" name="go" value="GO" class="ibutton" onclick="' + this.name + '.toPage(document.getElementById(\'pageInput' + this.showTimes + '\').value);"></option>';
	}
	strHtml += '</span>';
	<!-- end Input Box -->
	strHtml += '</div>';
	return strHtml;
}
showPages.prototype.createUrl = function (page) { //生成页面跳转url
	if (isNaN(parseInt(page))) page = 1;
	if (page < 1) page = 1;
	if (page > this.pageCount) page = this.pageCount;
	var url = location.protocol + '//' + location.host + location.pathname;
	var args = location.search;
	var reg = new RegExp('([\?&]?)' + this.argName + '=[^&]*[&$]?', 'gi');
	args = args.replace(reg,'$1');
	if (args == '' || args == null) {
		args += '?' + this.argName + '=' + page;
	} else if (args.substr(args.length - 1,1) == '?' || args.substr(args.length - 1,1) == '&') {
			args += this.argName + '=' + page;
	} else {
			args += '&' + this.argName + '=' + page;
	}
	return url + args;
}
showPages.prototype.toPage = function(page){ //页面跳转
	var turnTo = 1;
	if (typeof(page) == 'object') {
		turnTo = page.options[page.selectedIndex].value;
	} else {
		turnTo = page;
	}
	self.location.href = this.createUrl(turnTo);
}
showPages.prototype.printHtml = function(){ //显示html代码
	this.getPage();
	this.checkPages();
	this.showTimes += 1;
	document.write('<div id="pages_' + this.name + '_' + this.showTimes + '" class="pages"></div>');
	document.getElementById('pages_' + this.name + '_' + this.showTimes).innerHTML = this.createHtml();
	
}
showPages.prototype.formatInputPage = function(e){ //限定输入页数格式
	var ie = navigator.appName=="Microsoft Internet Explorer"?true:false;
	if(!ie) var key = e.which;
	else var key = event.keyCode;
	if (key == 8 || key == 46 || (key >= 48 && key <= 57)) return true;
	return false;
}

/*
 * Regex
 */

patrn_ACCOUNT = /^\w{6,20}$/;
patrn_PASSWORD = /^\w{6,20}$/;
patrn_NAME = /^[a-zA-Z]{1,20}$/;
patrn_EMAIL = /^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/;
patrn_CITY = /^[a-zA-Z ]{1,20}$/;
patrn_PHONE = /^[1-9]\d{2}[1-9]\d{6}$/;
patrn_ZIP = /^\d{5}$/;
patrn_RECIPIENT = /^[a-zA-Z ]{1,40}$/;
patrn_ADDRESS = /^.{1,250}$/;
patrn_CREDITNUM = /^\d{16}$/;
patrn_CSC = /^\d{3}$/;

message_ACCOUNT = "Only characters, numbers or _ are allowed; length: 6-20";
message_PASSWORD = "Only characters, numbers or _ are allowed; length: 6-20";
message_PASSWORDCOnFIRM = "Password should match";
message_FIRST = "Only characters; length: 1-20";
message_MIDDLE = "Only characters; length: 1-20";
message_LAST = "Only characters; length: 1-20";
message_GENDER = "Please select a gender";
message_BIRTHDAY = "Please input valid date";
message_OCCUPATION = "Please select an occupation";
message_EMAIL = "The format is invalid";
message_PHONE = "Please input 10 digit";
message_CITY = "Only characters and space allowed";
message_STATE = "Please select a state";
message_ZIP = "Please input 5 digit Zip code";
message_RECIPIENT = "Only characters and space; length: 6-40";
message_ADDRESS = "max length: 250";
message_CREDITNUM = "Please input 16 digit";
message_CREDITTYPE = "Please select a credit type";
message_EXPIRE = "Please select a date";
message_CSC = "Please input 3 digit CSC code";

/*
 * AJAX
 */
//AJAX 注册
//Format Validation
function registration_formatValidation(){
	account = document.getElementsByName("account")[0].value;
	password = document.getElementsByName("password")[0].value;
	password_confirm = document.getElementsByName("password_confirm")[0].value;
	first = document.getElementsByName("first")[0].value;
	middle = document.getElementsByName("middle")[0].value;
	last = document.getElementsByName("last")[0].value;
	gender = document.getElementsByName("gender")[0].value;
	birthday = document.getElementsByName("birthday")[0].value;
	occupation = document.getElementsByName("occupation")[0].value;
	email = document.getElementsByName("email")[0].value;
	phone = document.getElementsByName("phone")[0].value;
	city = document.getElementsByName("city")[0].value;
	state = document.getElementsByName("state")[0].value;
	zip = document.getElementsByName("zip")[0].value;

	message_reset();
	count = 0;
	
	if(!patrn_ACCOUNT.exec(account)){
			count++;
			document.getElementsByName("account")[1].textContent = message_ACCOUNT;
		}
		if(!patrn_PASSWORD.exec(password)){
			count++;
			document.getElementsByName("password")[1].textContent = message_PASSWORD;
		}
		if(password != password_confirm){
			count++;
			document.getElementsByName("password_confirm")[1].textContent = message_PASSWORDCOnFIRM;
		}
		if(!patrn_NAME.exec(first)){
			count++;
			document.getElementsByName("first")[1].textContent = message_FIRST;
		}
		if(middle != "" && !patrn_NAME.exec(middle)){
			count++;
			document.getElementsByName("middle")[1].textContent = message_MIDDLE;
		}
		if(!patrn_NAME.exec(last)){
			count++;
			document.getElementsByName("last")[1].textContent = message_LAST;
		}
		if(!gender){
			count++;
			document.getElementsByName("gender")[1].textContent = message_GENDER;
		}
		if(!birthday){
			count++;
			document.getElementsByName("birthday")[1].textContent = message_BIRTHDAY;
		}
		if(!occupation){
			count++;
			document.getElementsByName("occupation")[1].textContent = message_OCCUPATION;
		}
		if(!patrn_EMAIL.exec(email)){
			count++;
			document.getElementsByName("email")[1].textContent = message_EMAIL;
		}
		if(!patrn_PHONE.exec(phone)){
			count++;
			document.getElementsByName("phone")[1].textContent = message_PHONE;
		}
		if(!patrn_CITY.exec(city)){
			count++;
			document.getElementsByName("city")[1].textContent = message_CITY;
		}
		if(!state){
			count++;
			document.getElementsByName("state")[1].textContent = message_STATE;
		}
		if(!patrn_ZIP.exec(zip)){
			count++;
			document.getElementsByName("zip")[1].textContent = message_ZIP;
		}
		return count;
}
//Registration Post
function js_registration(){
	//Validation of Existence for Account
	$.post(location.protocol + '//' + location.host + "/ajax_validate_account/",
			{'account':document.getElementsByName("account")[0].value},
			function(ret){
				if(ret == '0'){
					if(! registration_formatValidation())
						$.post(location.protocol + '//' 
							  	+ location.host + "/ajax_register/",
							  	{'account':document.getElementsByName("account")[0].value,
							  		'password':document.getElementsByName("password")[0].value,
							  		'first':document.getElementsByName("first")[0].value,
							  		'middle':document.getElementsByName("middle")[0].value,
							  		'last':document.getElementsByName("last")[0].value,
							  		'gender':document.getElementsByName("gender")[0].value,
							  		'birthday':document.getElementsByName("birthday")[0].value,
							  		'occupation':document.getElementsByName("occupation")[0].value,
							  		'email':document.getElementsByName("email")[0].value,
							  		'phone':document.getElementsByName("phone")[0].value,
							  		'city':document.getElementsByName("city")[0].value,
							  		'state':document.getElementsByName("state")[0].value,
							  		'zip':document.getElementsByName("zip")[0].value},
						  		 function() {
							  		alert("Register successfully! You can sign in now.");
							  		self.location.href = "/login/";
							  		});
				}
				else
					document.getElementsByName("account")[1].textContent = "Account Exist! ";
			});
}


/*
 * Ajax登陆
 */
function js_login(){
	$.post(location.protocol + '//' 
		  	+ location.host + "/ajax_login/",
		  {'account':document.getElementsByName("account")[0].value,
		  	'password':document.getElementsByName("password")[0].value},
		  	function(ret) {
		  		if(ret == '1'){
		  			self.location.href = "/"
		  		}else
		  			alert("Invalid account or password. Please input again.");
		  });
}

/*
 * AJAX Profile update
 */
function js_profile_update(){
	if(!profile_formatValidation())
		$.post(location.protocol + '//' 
			  	+ location.host + "/ajax_modify_profile/",
			  		{'first':document.getElementsByName("first")[0].value,
			  		'middle':document.getElementsByName("middle")[0].value,
			  		'last':document.getElementsByName("last")[0].value,
			  		'gender':document.getElementsByName("gender")[0].value,
			  		'birthday':document.getElementsByName("birthday")[0].value,
			  		'occupation':document.getElementsByName("occupation")[0].value,
			  		'email':document.getElementsByName("email")[0].value,
			  		'phone':document.getElementsByName("phone")[0].value,
			  		'city':document.getElementsByName("city")[0].value,
			  		'state':document.getElementsByName("state")[0].value,
			  		'zip':document.getElementsByName("zip")[0].value},
		  		 function() {
			  		alert("Update successfully!")
			  		self.location.href = "/view_profile/"
			  		});
}

function profile_formatValidation(){
	first=document.getElementsByName("first")[0].value;
    middle=document.getElementsByName("middle")[0].value;
    last=document.getElementsByName("last")[0].value;
    birthday=document.getElementsByName("birthday")[0].value;
    gender=document.getElementsByName("gender")[0].value;
    occupation=document.getElementsByName("occupation")[0].value;
    email=document.getElementsByName("email")[0].value;
    phone=document.getElementsByName("phone")[0].value;
    city=document.getElementsByName("city")[0].value;
    state=document.getElementsByName("state")[0].value;
    zip=document.getElementsByName("zip")[0].value;
    
    message_reset();
    count = 0;
    
	if(!patrn_NAME.exec(first)){
		count++;
		document.getElementsByName("first")[1].textContent = message_FIRST;
	}
	if(middle != "" && !patrn_NAME.exec(middle)){
		count++;
		document.getElementsByName("middle")[1].textContent = message_MIDDLE;
	}
	if(!patrn_NAME.exec(last)){
		count++;
		document.getElementsByName("last")[1].textContent = message_LAST;
	}
	if(!gender){
		count++;
		document.getElementsByName("gender")[1].textContent = message_GENDER;
	}
	if(!birthday){
		count++;
		document.getElementsByName("birthday")[1].textContent = message_BIRTHDAY;
	}
	if(!occupation){
		count++;
		document.getElementsByName("occupation")[1].textContent = message_OCCUPATION;
	}
	if(!patrn_EMAIL.exec(email)){
		count++;
		document.getElementsByName("email")[1].textContent = message_EMAIL;
	}
	if(!patrn_PHONE.exec(phone)){
		count++;
		document.getElementsByName("phone")[1].textContent = message_PHONE;
	}
	if(!patrn_CITY.exec(city)){
		count++;
		document.getElementsByName("city")[1].textContent = message_CITY;
	}
	if(!state){
		count++;
		document.getElementsByName("state")[1].textContent = message_STATE;
	}
	if(!patrn_ZIP.exec(zip)){
		count++;
		document.getElementsByName("zip")[1].textContent = message_ZIP;
	}
    return count;
}
/*
 * AJAX update password
 */
function js_password_update(){
	if(!password_formatValidation())
		$.post(location.protocol + '//' 
				  	+ location.host + "/ajax_password_modify/",
				  {'oldpassword' : document.getElementsByName("oldpassword")[0].value,
					'newpassword':document.getElementsByName("newpassword")[0].value},
				  	function(ret){
					  if(ret == "1"){
						  alert("Password modify successfully!");
						  self.location.href = "/view_profile/";
					  }else if(ret == "0")
						  document.getElementsByName("oldpassword")[1].textContent = message_PASSWORD;

				  });
}

function password_formatValidation(){
	newpassword = document.getElementsByName("newpassword")[0].value;
	confirmpassword = document.getElementsByName("confirmpassword")[0].value;
	
	message_reset();
	count = 0;
	
	if(!patrn_PASSWORD.exec(newpassword)){
		count++;
		document.getElementsByName("newpassword")[1].textContent = message_PASSWORD;
	}
	if(newpassword != confirmpassword){
		count++;
		document.getElementsByName("confirmpassword")[1].textContent = message_PASSWORDCOnFIRM;
	}
	return count;
}

/*
 * AJAX update shipping(user, order)
 */
function js_userShipping_update(){
	if(!shipping_formatValidation())	
		$.post(location.protocol + '//' 
			  	+ location.host + "/ajax_usershipping_modify/",
			  {"shipping_to" : document.getElementsByName("shipping_to")[0].value,
			    "shipping_address" : document.getElementsByName("shipping_address")[0].value,
			    "shipping_city" : document.getElementsByName("shipping_city")[0].value,
			    "shipping_state" : document.getElementsByName("shipping_state")[0].value,
			    "shipping_zip" : document.getElementsByName("shipping_zip")[0].value,
			    "shipping_phone" : document.getElementsByName("shipping_phone")[0].value},
			  	function(ret){
				  if(ret == "1"){
					  alert("Shipping update successfully!");
					  self.location.href = "/view_shipping/";
				  }
			    });
}

function shipping_formatValidation(){
    shipping_to = document.getElementsByName("shipping_to")[0].value;
    shipping_address = document.getElementsByName("shipping_address")[0].value;
    shipping_city = document.getElementsByName("shipping_city")[0].value;
    shipping_state = document.getElementsByName("shipping_state")[0].value;
    shipping_zip = document.getElementsByName("shipping_zip")[0].value;
    shipping_phone = document.getElementsByName("shipping_phone")[0].value;
    
    message_reset()
    count = 0;
	
    if(!patrn_RECIPIENT.exec(shipping_to)){
		count++;
		document.getElementsByName("shipping_to")[1].textContent = message_RECIPIENT;
	}
	if(!patrn_ADDRESS.exec(shipping_address)){
		count++;
		document.getElementsByName("shipping_address")[1].textContent = message_ADDRESS;
	}
	if(!patrn_CITY.exec(shipping_city)){
		count++;
		document.getElementsByName("shipping_city")[1].textContent = message_CITY;
	}
	if(!shipping_state){
		count++;
		document.getElementsByName("shipping_state")[1].textContent = message_STATE;
	}
	if(!patrn_ZIP.exec(shipping_zip)){
		count++;
		document.getElementsByName("shipping_zip")[1].textContent = message_ZIP;
	}
	if(!patrn_PHONE.exec(shipping_phone)){
		count++;
		document.getElementsByName("shipping_phone")[1].textContent = message_PHONE;
	}
	return count;
}
/*
 * AJAX credit update(User & Order)
 */
//update user credit
function js_userCredit_update(){
	if(!credit_formatValidation())
		$.post(location.protocol + '//' 
			  	+ location.host + "/ajax_usercredit_modify/",
			  {"creidt_number" : document.getElementsByName("creidt_number")[0].value,
			    "creidt_type" : document.getElementsByName("creidt_type")[0].value,
			    "creidt_expire" : document.getElementsByName("creidt_expire")[0].value + "-01",
			    "creidt_csc" : document.getElementsByName("creidt_csc")[0].value,
			    "creidt_holder" : document.getElementsByName("creidt_holder")[0].value,
			    "creidt_address" : document.getElementsByName("creidt_address")[0].value,
			    "creidt_city" : document.getElementsByName("creidt_city")[0].value,
			    "creidt_state" : document.getElementsByName("creidt_state")[0].value,
			    "creidt_zip" : document.getElementsByName("creidt_zip")[0].value},
			  	function(ret){
				  if(ret == "1"){
					  alert("Credit update successfully!");
					  self.location.href = "/view_credit/";
				  }
			    });
}

function credit_formatValidation(){
	creidt_number = document.getElementsByName("creidt_number")[0].value;
    creidt_type = document.getElementsByName("creidt_type")[0].value;
    creidt_expire = document.getElementsByName("creidt_expire")[0].value;
    creidt_csc = document.getElementsByName("creidt_csc")[0].value;
    creidt_holder = document.getElementsByName("creidt_holder")[0].value;
    creidt_address = document.getElementsByName("creidt_address")[0].value;
    creidt_city = document.getElementsByName("creidt_city")[0].value;
    creidt_state = document.getElementsByName("creidt_state")[0].value;
    creidt_zip = document.getElementsByName("creidt_zip")[0].value;
    
    message_reset()
    count = 0;
    
    if(!patrn_CREDITNUM.exec(creidt_number)){
		count++;
		document.getElementsByName("creidt_number")[1].textContent = message_CREDITNUM;
	}
    if(!creidt_type){
		count++;
		document.getElementsByName("creidt_type")[1].textContent = message_CREDITTYPE;
	}
    if(!creidt_expire){
		count++;
		document.getElementsByName("creidt_expire")[1].textContent = message_EXPIRE;
	}
    if(!patrn_CSC.exec(creidt_csc)){
		count++;
		document.getElementsByName("creidt_csc")[1].textContent = message_CSC;
	}
    if(!patrn_RECIPIENT.exec(creidt_holder)){
		count++;
		document.getElementsByName("creidt_holder")[1].textContent = message_RECIPIENT;
	}
    if(!patrn_ADDRESS.exec(creidt_address)){
		count++;
		document.getElementsByName("creidt_address")[1].textContent = message_ADDRESS;
	}
    if(!patrn_CITY.exec(creidt_city)){
		count++;
		document.getElementsByName("creidt_city")[1].textContent = message_CITY;
	}
    if(!creidt_state){
		count++;
		document.getElementsByName("creidt_state")[1].textContent = message_STATE;
	}
    if(!patrn_ZIP.exec(creidt_zip)){
		count++;
		document.getElementsByName("creidt_zip")[1].textContent = message_ZIP;
	}
  
    return count;
}

//reset
function reset(){
	input_reset();
	message_reset();
}
//input reset
function input_reset(){
	for(var i=0;i<$("td.input input").length;i++){
		$("td.input input")[i].value = "";
	}
	for(var i=0;i<$("td select").length;i++){
		$("td select")[i].value = "";
	}
}

//message reset
function message_reset(){
	for(var i=0;i<$("td.message").length;i++){
		$("td.message")[i].textContent = "";
	}
}
/*
 * AJAX add an item
 */
function js_addItem(id){
	$.get(location.protocol + '//' + location.host + "/ajax_additem/?id=" + id,
			function(ret){
			/*
			 * -1 not login
			 * 0 out of stock
			 * 1 success
			 * 2 ready in
			 */
			if(ret == "-1"){
				alert("Please login first!");
				self.location.href = "/login/";
			}else if(ret == "0"){
				alert("Sorry, this product is out of stock.");
			}else if(ret == "1"){
				if(!confirm("This item has been added to your cart.\n Do you want to continue shopping?"))
					self.location.href = "/modify_order/";
			}else if(ret == "2"){
				if(!confirm("This item is already in your cart.\n Do you want to continue shopping?"))
					self.location.href = "/modify_order/";
			}else
				alert("error!");
	});
}

function js_updateitemquantity(id,order_id, quantity,avaliable_quan){
	if(quantity <= 0){
		if(confirm("Do you want to remove this item from your cart?")){
			$.post(location.protocol + '//' 
				  	+ location.host + "/ajax_updateitemquantity/",
				  {"id" : id,
					"quantity" : quantity},
				  	function(ret){});
			$.post(location.protocol + '//' 
				  	+ location.host + "/ajax_check_deleteorder/",
				  {"id" : order_id},
				  	function(ret){
					  if(ret == "0"){
						  alert("Your cart is empty.");
						  self.location.href = "/view_order_list/?page=1";
					  }else
						  location.reload();
				    });
		}else
			location.reload();
	}else if (quantity >  avaliable_quan){
		alert("Sorry,There are only "  + avaliable_quan +" of this items in avaliable.");
		location.reload();
	}else
		$.post(location.protocol + '//' 
			  	+ location.host + "/ajax_updateitemquantity/",
			  {"id" : id,
				"quantity" : quantity},
			  	function(ret){
					alert("Update successfully!");
					location.reload();
				});
}

function js_updateitempromotion(id, order_id, movie_id, code){
	$.post(location.protocol + '//' 
		  	+ location.host + "/ajax_updateitempromotion/",
		  {"id" : id,
		  	'order_id' : order_id,
		  	'movie_id' : movie_id,
		  	'code' : code},
		  	function(ret){
				  if(ret == "0"){
					  alert("Sorry. The promotion code is invalid!");
					  location.reload();
				  }else if(ret == "-1"){
					  alert("Sorry. Please wait until this promotion start!");
					  location.reload();
				  }else if(ret == "-2"){
					  alert("Sorry. This promotion is out of date!");
					  location.reload();
				  }else if(ret == "1"){
					  alert("The promotion code has been added successfully!");
					  location.reload();
				  }else if(ret == "2"){
					  alert("The promotion code has been removed successfully!");
					  location.reload();
				  }
		  	});
	
}

function js_updateordershipping(id){
	if(!shipping_formatValidation())
		$.post(location.protocol + '//' 
			  	+ location.host + "/ajax_ordershipping_modify/",
			  {"id" : id,
				"shipping_to" : document.getElementsByName("shipping_to")[0].value,
			    "shipping_address" : document.getElementsByName("shipping_address")[0].value,
			    "shipping_city" : document.getElementsByName("shipping_city")[0].value,
			    "shipping_state" : document.getElementsByName("shipping_state")[0].value,
			    "shipping_zip" : document.getElementsByName("shipping_zip")[0].value,
			    "shipping_phone" : document.getElementsByName("shipping_phone")[0].value},
			  	function(ret){
				  if(ret == "1"){
					  alert("Shipping update successfully!");
					  self.location.href = "/modify_order/";
				  }
			    });
}

function js_updateordercredit(id){
	if(!credit_formatValidation())
		$.post(location.protocol + '//' 
			  	+ location.host + "/ajax_ordercredit_modify/",
			  {"id" : id,
				"creidt_number" : document.getElementsByName("creidt_number")[0].value,
				"creidt_type" : document.getElementsByName("creidt_type")[0].value,
				"creidt_expire" : document.getElementsByName("creidt_expire")[0].value + "-01",
				"creidt_csc" : document.getElementsByName("creidt_csc")[0].value,
				"creidt_holder" : document.getElementsByName("creidt_holder")[0].value,
				"creidt_address" : document.getElementsByName("creidt_address")[0].value,
				"creidt_city" : document.getElementsByName("creidt_city")[0].value,
				"creidt_state" : document.getElementsByName("creidt_state")[0].value,
				"creidt_zip" : document.getElementsByName("creidt_zip")[0].value},
			  	function(ret){
				  if(ret == "1"){
					  alert("Shipping update successfully!");
					  self.location.href = "/modify_order/";
				  }
			    });
}

function js_checkout(id){
	$.post(location.protocol + '//' 
		  	+ location.host + "/ajax_checkout/",
		  {"id" : id},
		  	function(ret){
			  if(ret == "-1"){
				  alert("Please fill the shipping information before checking out.");
				  self.location.href = "/modifyordershipping_page/?id=" + id;
			  }else if(ret == "-2"){
				  alert("Please fill the credit information before checking out.");
				  self.location.href = "/modifyordercredit_page/?id=" + id;
			  }else if(ret == "1"){
				  alert("Check out successfully!");
				  self.location.href = "/view_order_list/?page=1";
			  }else if(ret == "0"){
				  alert("Order doesn't exit");
				  self.location.href = "/view_order_list/?page=1";
			  }else{
				  error_message = ""
				  for(i in ret){
					  error_message += ret[i]['title'] + " :\n"
					  if(ret[i]['quantity'])
						  error_message += "There are only " + ret[i]['quantity'] + " in store.\n";
					  if(ret[i]['promotion'])
						  error_message += "The promotion is invalid. Please remove it.\n";
					  error_message +="\n";
				  }
				  alert(error_message);
			  }
		    });
}

//Admin
//Admin Login
function admin_js_login(){
	$.post(location.protocol + '//' 
		  	+ location.host + "/admin_ajax_login/",
		  {'account':document.getElementsByName("account")[0].value,
		  	'password':document.getElementsByName("password")[0].value},
		  	function(ret) {
		  		if(ret == '1'){
		  			self.location.href = "/admin_home/"
		  		}else
		  			alert("Invalid account or password. Please input again.");
		  });
}

function admin_js_profile_update(user_id){
	if(!profile_formatValidation())
		$.post(location.protocol + '//' 
			  	+ location.host + "/admin_ajax_modify_profile/",
			  		{'id' : user_id,
					'first':document.getElementsByName("first")[0].value,
			  		'middle':document.getElementsByName("middle")[0].value,
			  		'last':document.getElementsByName("last")[0].value,
			  		'gender':document.getElementsByName("gender")[0].value,
			  		'birthday':document.getElementsByName("birthday")[0].value,
			  		'occupation':document.getElementsByName("occupation")[0].value,
			  		'email':document.getElementsByName("email")[0].value,
			  		'phone':document.getElementsByName("phone")[0].value,
			  		'city':document.getElementsByName("city")[0].value,
			  		'state':document.getElementsByName("state")[0].value,
			  		'zip':document.getElementsByName("zip")[0].value},
		  		 function() {
			  		alert("Update successfully!");
			  		self.location.href = "/admin_viewcustomer/?id=" + user_id;
			  		});
}

function admin_js_adminprofile_update(user_id){
	if(!adminprofile_formatValidation())
		$.post(location.protocol + '//' 
			  	+ location.host + "/admin_ajax_modify_adminprofile/",
			  		{'id' : user_id,
					'first':document.getElementsByName("first")[0].value,
			  		'last':document.getElementsByName("last")[0].value},
		  		 function() {
			  		alert("Update successfully!");
			  		self.location.href = "/admin_viewadmin/?id=" + user_id;
			  		});
}

function adminprofile_formatValidation(){
first=document.getElementsByName("first")[0].value;
last=document.getElementsByName("last")[0].value;

message_reset();
count = 0;

if(!patrn_NAME.exec(first)){
	count++;
	document.getElementsByName("first")[1].textContent = message_FIRST;
}
if(!patrn_NAME.exec(last)){
	count++;
	document.getElementsByName("last")[1].textContent = message_LAST;
}
return count;
}



function admin_js_searchcustomer(){
	self.location.href = "/admin_findcustomer/?account="+ document.getElementsByName("account")[0].value +
	"&first=" + document.getElementsByName("first")[0].value + 
	"&last=" + document.getElementsByName("last")[0].value + "&page=1";
}

function admin_js_searchadmin(){
	self.location.href = "/admin_findadmin/?account="+ document.getElementsByName("account")[0].value +
	"&first=" + document.getElementsByName("first")[0].value + 
	"&last=" + document.getElementsByName("last")[0].value + "&page=1";
}

function admin_js_searchmovie(){
	self.location.href = "/admin_findmovie/?title="+ document.getElementsByName("title")[0].value +
	"&genre=" + document.getElementsByName("genre")[0].value + "&page=1";
}

function admin_js_searchorder(){
	self.location.href = "/admin_findorder/?account="+ document.getElementsByName("account")[0].value +
	"&status=" + document.getElementsByName("status")[0].value + "&page=1";
}

function admin_js_searchmoviewithpromotion(promotion_id){
	self.location.href = "/admin_promotion_removemovie_page/?id=" + promotion_id
	+ "&title="+ document.getElementsByName("title")[0].value +
	"&genre_id=" + document.getElementsByName("genre")[0].value + "&page=1";
	
}

function admin_js_searchmoviewithoutpromotion(promotion_id){
	self.location.href = "/admin_promotion_addmovie_page/?id=" + promotion_id
	+ "&title="+ document.getElementsByName("title")[0].value +
	"&genre_id=" + document.getElementsByName("genre")[0].value + "&page=1";
}

function admin_js_searchpromotion(){
	self.location.href = "/admin_findpromotion/?code="+ document.getElementsByName("code")[0].value +
	"&begin=" + document.getElementsByName("begin")[0].value + "&end=" + document.getElementsByName("end")[0].value + "&page=1";
	
}

function admin_js_password_update(user_id,user_type){
	if(!password_formatValidation()){
		$.post(location.protocol + '//' 
			  	+ location.host + "/admin_ajax_password_modify/",
			  {'id': user_id,
				'newpassword':document.getElementsByName("newpassword")[0].value},
			  	function(ret){
				  if(ret == "1"){
					  alert("Password modify successfully!");
					  if(user_type == '1')
						  self.location.href = "/admin_update_profile_page/?id=" + user_id;
					  else if(user_type == '0')
						  self.location.href = "/admin_update_adminprofile_page/?id=" + user_id;
				  }
			});
	}

}

/*Movie Detail*/
patrn_TITLE = /^[A-Za-z0-9]([A-Za-z0-9]|\s){0,40}$/;
patrn_DIRECTOR = /^([a-zA-Z]|\s){0,40}$/;
patrn_ACTOR = /^.{0,60}$/;
patrn_DESCRIPTION = /^.{0,200}$/;
patrn_PRICE = /^(([1-9]+\d*(\.[0-9]{1,2})?)|(0\.[0-9]{1,2}))$/;
patrn_QUANTITY = /^\d+$/;

message_TITLE = "Only characters,numbers or space are allowed; length: 1-40";
message_DIRECTOR = "Only characters and space are allowed; max length: 40";
message_ACTOR = "Only characters and space are allowed; max length: 60";
message_DESCRIPTION = "Max length: 200";
message_PRICE = "Float number(2 decimal places)";
message_QUANTITY = "Natural number";

function admin_checkmovie(){
		
	document.getElementsByName("title")[1].textContent = "";
	document.getElementsByName("year")[1].textContent = "";
	document.getElementsByName("director")[1].textContent = "";
	document.getElementsByName("actor")[1].textContent = "";
	document.getElementsByName("description")[1].textContent = "";
	document.getElementsByName("price")[1].textContent = "";
	document.getElementsByName("quantity")[1].textContent = "";
	
	count = 0;
	if(!patrn_TITLE.exec(document.getElementsByName("title")[0].value)){
		count++;
		document.getElementsByName("title")[1].textContent = message_TITLE;
	}
	if(!patrn_DIRECTOR.exec(document.getElementsByName("director")[0].value)){
		count++;
		document.getElementsByName("director")[1].textContent = message_DIRECTOR;
	}
	if(!patrn_ACTOR.exec(document.getElementsByName("actor")[0].value)){
		count++;
		document.getElementsByName("actor")[1].textContent = message_ACTOR;
	}
	if(!patrn_DESCRIPTION.exec(document.getElementsByName("description")[0].value)){
		count++;
		document.getElementsByName("description")[1].textContent = message_DESCRIPTION;
	}
	if(!patrn_PRICE.exec(document.getElementsByName("price")[0].value)){
		count++;
		document.getElementsByName("price")[1].textContent = message_PRICE;
	}
	if(!patrn_QUANTITY.exec(document.getElementsByName("quantity")[0].value)){
		count++;
		document.getElementsByName("quantity")[1].textContent = message_QUANTITY;
	}
	
	if(count == 0){
		if(confirm("Confirm to add a new movie!"))
			return true;
		else
			return false;
	}else
		return false;
}

/*Promotion*/
patrn_CODE = /^.{10,30}$/;
patrn_DISCOUNT = /^(100|[0-9]{1,2})$/;

message_CODE = "Length : 10-30";
message_DISCOUNT = "Natural number(0 - 100)";

function admin_checkpromotion(){
	
	document.getElementsByName("code")[1].textContent = "";
	document.getElementsByName("begin")[1].textContent = "";
	document.getElementsByName("end")[1].textContent = "";
	document.getElementsByName("discount")[1].textContent = "";
	
	count = 0;
	$.post(location.protocol + '//' 
		  	+ location.host + "/admin_ajax_code_isexisted/",
		  {'code':document.getElementsByName("code")[0].value},
		  	function(ret){
			  if(ret == "1"){
				  document.getElementsByName("code")[1].textContent = "Code exist";
				  count++;
			  }else if(ret == "0"){
				  if(!patrn_CODE.exec(document.getElementsByName("code")[0].value)){
					  document.getElementsByName("code")[1].textContent = message_CODE;
					  count++;
				  }
			  }else{
				  alert("error");
			  }
		});
	if(document.getElementsByName("begin")[0].value == ""){
		document.getElementsByName("begin")[1].textContent = "Please input starting date";
		count++;
	}
	if(document.getElementsByName("end")[0].value == ""){
		document.getElementsByName("end")[1].textContent = "Please input end date";
		count++;
	}
	if(document.getElementsByName("begin")[0].value != "" && document.getElementsByName("end")[0].value != ""){
		if(new Date(document.getElementsByName("begin")[0].value) > new Date(document.getElementsByName("end")[0].value)){
			document.getElementsByName("begin")[1].textContent = "Starting date should be same or after the end date";
			count++;
		}
	}
	if(!patrn_DISCOUNT.exec(document.getElementsByName("discount")[0].value)){
		document.getElementsByName("discount")[1].textContent = message_DISCOUNT;
		count++;
	}
	
	if(count == 0){
		if(confirm("Confirm to add a new promotion!"))
			return true;
		else
			return false;
	}else
		return false;
}

function admin_checkpromotion_begin_end_discount(){
	
	document.getElementsByName("begin")[1].textContent = "";
	document.getElementsByName("end")[1].textContent = "";
	document.getElementsByName("discount")[1].textContent = "";
	
	count = 0;
	if(document.getElementsByName("begin")[0].value == ""){
		document.getElementsByName("begin")[1].textContent = "Please input starting date";
		count++;
	}
	if(document.getElementsByName("end")[0].value == ""){
		document.getElementsByName("end")[1].textContent = "Please input end date";
		count++;
	}
	if(document.getElementsByName("begin")[0].value != "" && document.getElementsByName("end")[0].value != ""){
		if(new Date(document.getElementsByName("begin")[0].value) > new Date(document.getElementsByName("end")[0].value)){
			document.getElementsByName("begin")[1].textContent = "Starting date should be same or after the end date";
			count++;
		}
	}
	if(!patrn_DISCOUNT.exec(document.getElementsByName("discount")[0].value)){
		document.getElementsByName("discount")[1].textContent = message_DISCOUNT;
		count++;
	}
	
	if(count == 0){
		if(confirm("Confirm to update promotion!"))
			return true;
		else
			return false;
	}else
		return false;
}

function toggle(source){
	checkboxes = document.getElementsByName('check');
	for(var i=0;i<checkboxes.length;i++){
		document.getElementsByName('check')[i].checked = source.checked;
	}
}

function checkAllAndReset(boo){
	checkboxes = document.getElementsByName('check');
	for(var i=0;i<checkboxes.length;i++){
		document.getElementsByName('check')[i].checked = boo;
	}
}

function ajax_addMovieToPromotion(promotionid){
	var movieid_list = [];
	checkboxes = document.getElementsByName('check');
	for(var i=0;i<checkboxes.length;i++){
		if(document.getElementsByName('check')[i].checked)
			movieid_list.push(document.getElementsByName('check')[i].value);
	}
	$.post(location.protocol + '//' 
		  	+ location.host + "/admin_ajax_promotion_addmovie/",
		  {'promotionid' : promotionid,
			'movieid_list' : movieid_list},
		  	function(ret) {
		  		if(ret == '1'){
		  			alert("Promotion has been added to movies successfully.");
		  			location.reload();
		  		}else
		  			alert("Invalid account or password. Please input again.");
		  });
}

function ajax_removeMovieFromPromotion(promotionid){
	var movieid_list = [];
	checkboxes = document.getElementsByName('check');
	for(var i=0;i<checkboxes.length;i++){
		if(document.getElementsByName('check')[i].checked)
			movieid_list.push(document.getElementsByName('check')[i].value);
	}
	$.post(location.protocol + '//' 
		  	+ location.host + "/admin_ajax_promotion_removemovie/",
		  {'promotionid' : promotionid,
			'movieid_list' : movieid_list},
		  	function(ret) {
		  		if(ret == '1'){
		  			alert("Promotion has been removed from movies successfully.");
		  			location.reload();
		  		}else
		  			alert("Invalid account or password. Please input again.");
		  });
}

function confirmToDelete(url){
	if(confirm("Confirm to Delete!"))
		self.location.href = url;
}

function popAlert(message){
	alert(message);
	return true;
}

function addadmin_formatValidation(){
	account = document.getElementsByName("account")[0].value;
	password = document.getElementsByName("password")[0].value;
	password_confirm = document.getElementsByName("password_confirm")[0].value;
	first = document.getElementsByName("first")[0].value;
	last = document.getElementsByName("last")[0].value;

	message_reset();
	count = 0;
	
	if(!patrn_ACCOUNT.exec(account)){
			count++;
			document.getElementsByName("account")[1].textContent = message_ACCOUNT;
		}
		if(!patrn_PASSWORD.exec(password)){
			count++;
			document.getElementsByName("password")[1].textContent = message_PASSWORD;
		}
		if(password != password_confirm){
			count++;
			document.getElementsByName("password_confirm")[1].textContent = message_PASSWORDCOnFIRM;
		}
		if(!patrn_NAME.exec(first)){
			count++;
			document.getElementsByName("first")[1].textContent = message_FIRST;
		}
		if(!patrn_NAME.exec(last)){
			count++;
			document.getElementsByName("last")[1].textContent = message_LAST;
		}
		return count;
}

function js_addadmin(){
	//Validation of Existence for Account
	$.post(location.protocol + '//' + location.host + "/ajax_validate_account/",
			{'account':document.getElementsByName("account")[0].value},
			function(ret){
				if(ret == '0'){
					if(! addadmin_formatValidation())
						$.post(location.protocol + '//' 
							  	+ location.host + "/admin_addadmin/",
							  	{'account':document.getElementsByName("account")[0].value,
							  		'password':document.getElementsByName("password")[0].value,
							  		'first':document.getElementsByName("first")[0].value,
							  		'last':document.getElementsByName("last")[0].value},
						  		 function() {
							  		alert("Admin has been created successfully!");
							  		self.location.href = "/admin_findadmin/?account=&first=&last=&page=1";
							  		});
				}
				else{
					document.getElementsByName("account")[1].textContent = "Account Exist! ";
				}
					
			});
}