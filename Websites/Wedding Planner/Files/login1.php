<body>

<form method="post" action="panel2.php" class="login">

    <p>
      <label for="login">Username:</label>
      <input type="text" name="name" id="login" value="Enter username">
    </p>

    <p>
      <label for="password">Password:</label>
      <input type="password" name="pass" id="password" value="Enter password">
    </p>

    <p class="login-submit">
      <button type="submit" class="login-button" name="login"><a href="panel2.php">Login</button>
    </p>

    <p class="forgot-password" onclick="popup()">Forgot your password?</a></p>
        <p class="forgot-password" ><a href="register1.php">Don't have an account? Sign up</a></p>
  </form>
<script type="text/javascript">
  function popup(){
var age = parseInt(prompt("Please enter your email address:"));
if(age=""){
  alert("Enter email id")
}
else{
  alert("Thankyou! Please check your email id for the new password")
}
}
</script>




<style type="text/css">

body, .login-submit, .login-submit:before, .login-submit:after {
    background-color:#a2aad2;

}

body {
  font: 14px/20px 'Helvetica Neue', Helvetica, Arial, sans-serif;
  color: #404040;
}

a {
  color: #00a1d2;
  text-decoration: none;
}
a:hover {
  text-decoration: underline;
}

.login {
  position: relative;
  margin: 80px auto;
  width: 400px;
  padding-right: 32px;
  font-weight: 300;

  text-shadow: 1px 1px 0 rgba(0, 0, 0, 0.8);
}
.login p {
  margin: 0 0 10px;
}

input, button, label {
  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  font-size: 15px;
  font-weight: 300;
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;

}

input[type=text], input[type=password] {
  padding: 0 10px;
  width: 300px;
  height: 40px;
  color: #bbb;
  text-shadow: 1px 1px 1px black;
  background: rgba(0, 0, 0, 0.16);
  border: 0;
  border-radius: 5px;
  -webkit-box-shadow: inset 0 1px 4px rgba(0, 0, 0, 0.3), 0 1px rgba(255, 255, 255, 0.06);
  box-shadow: inset 0 1px 4px rgba(0, 0, 0, 0.3), 0 1px rgba(255, 255, 255, 0.06);
}
input[type=text]:focus, input[type=password]:focus {
  color: white;
  background: rgba(0, 0, 0, 0.1);
  outline: 0;
}

label {
  float: left;
  width: 100px;
  line-height: 40px;
  padding-right: 10px;
  font-weight: 100;
  text-align: right;
  letter-spacing: 1px;
}

.forgot-password {
  padding-left: 100px;
  font-size: 13px;
  font-weight: 100;
  letter-spacing: 1px;
  cursor: pointer;
}

.login-submit {
  position: absolute;
  top: 12px;
  right: 0;
  width: 48px;
  height: 48px;
  padding: 8px;
  border-radius: 32px;
  -webkit-box-shadow: 0 0 4px rgba(0, 0, 0, 0.35);
  box-shadow: 0 0 4px rgba(0, 0, 0, 0.35);
}
.login-submit:before, .login-submit:after {
  content: '';
  z-index: 1;
  position: absolute;
}
.login-submit:before {
  top: 28px;
  left: -4px;
  width: 4px;
  height: 10px;
  -webkit-box-shadow: inset 0 1px rgba(255, 255, 255, 0.06);
  box-shadow: inset 0 1px rgba(255, 255, 255, 0.06);
}
.login-submit:after {
  top: -4px;
  bottom: -4px;
  right: -4px;
  width: 36px;
}

.login-button {
  position: relative;
  z-index: 2;
  width: 48px;
  height: 48px;
  padding: 0 0 48px;
  /* Fix wrong positioning in Firefox 9 & older (bug 450418) */
  text-indent: 120%;
  white-space: nowrap;
  overflow: hidden;
  background: none;
  border: 0;
  border-radius: 24px;
  cursor: pointer;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.2), 0 1px rgba(255, 255, 255, 0.1);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.2), 0 1px rgba(255, 255, 255, 0.1);
  /* Must use another pseudo element for the gradient background because Webkit */
  /* clips the background incorrectly inside elements with a border-radius.     */
}
.login-button:before {
  content: '';
  position: absolute;
  top: 5px;
  bottom: 5px;
  left: 5px;
  right: 5px;
  background: #00a2d3;
  border-radius: 24px;
  background-image: -webkit-linear-gradient(top, #00a2d3, #0d7796);
  background-image: -moz-linear-gradient(top, #00a2d3, #0d7796);
  background-image: -o-linear-gradient(top, #00a2d3, #0d7796);
  background-image: linear-gradient(to bottom, #00a2d3, #0d7796);
  -webkit-box-shadow: inset 0 0 0 1px #00a2d3, 0 0 0 5px rgba(0, 0, 0, 0.16);
  box-shadow: inset 0 0 0 1px #00a2d3, 0 0 0 5px rgba(0, 0, 0, 0.16);
}
.login-button:active:before {
  background: #0591ba;
  background-image: -webkit-linear-gradient(top, #0591ba, #00a2d3);
  background-image: -moz-linear-gradient(top, #0591ba, #00a2d3);
  background-image: -o-linear-gradient(top, #0591ba, #00a2d3);
  background-image: linear-gradient(to bottom, #0591ba, #00a2d3);
}
.login-button:after {
  content: '';
  position: absolute;
  top: 15px;
  left: 12px;
  width: 25px;
  height: 19px;
  background: url("http://s3.cssflow.com/snippets/23-dark-login-form/img/arrow.png") 0 0 no-repeat;
}

::-moz-focus-inner {
  border: 0;
  padding: 0;
}

.lt-ie9 input[type=text], .lt-ie9 input[type=password] {
  line-height: 40px;
  background: #282828;
}
.lt-ie9 .login-submit {
  position: absolute;
  top: 12px;
  right: -28px;
  padding: 4px;
}
.lt-ie9 .login-submit:before, .lt-ie9 .login-submit:after {
  display: none;
}
.lt-ie9 .login-button {
  line-height: 48px;
}
.lt-ie9 .about {
  background: #313131;
}
</style>



</body>
