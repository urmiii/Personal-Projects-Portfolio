<link rel="stylesheet" type="text/css" href="panel2.css">
<link rel="stylesheet" type="text/css" href="home.css">
<header>
  <h1 class="site-title">
    Admin Panel
  </h1>

  <div class="card">
<br>
&nbsp&nbsp&nbsp&nbsp
<label class="switch"> Icons 
  <input type="checkbox" checked>
  <span class="slider round"></span>
</label>  
<br><br><br>
&nbsp&nbsp&nbsp&nbsp
<label class="switch"> Refresh 
  <input type="checkbox" checked>
  <span class="slider round"></span>
</label> 
<br><br><br>
&nbsp&nbsp&nbsp&nbsp
<label class="switch"> Autooptimzation 
  <input type="checkbox" checked>
  <span class="slider round"></span>
</label> 


</div>

   </div>

</header>

<div class="container">

  <div class="navbar">
    <ul class="nav">
      <li class="nav-item">
        <a href="panel2.php">Home</a>

      </li>

      <li class="nav-item">
        <a href="USERPANEL2.php">Users</a>

      </li>

      <li class="nav-item">
        <a href="venue.php">Venue</a>
      </li>

      <li class="nav-item">
        <a href="/statistics">Gallery</a>
      </li>
    </ul>
  </div>
  <div class="content">

  </div>

</div>
<style type="text/css">
  html {
  font-size: 62.5%; /* resets base font-size to 10px, which makes 'rems' easier to mentally calculate for the user */
  box-sizing: border-box;
}

body {
  margin: 0;
  padding: 0;
  font-family: Verdana, Helvetica, Arial, sans-serif;
  font-size: 1.6rem;
}

header {
  background-color:#606eb2;
  min-height: 150px;
  color: #ffffff;
  
  position: relative;
}

header div:first-of-type {
  margin: 0;
  color: #fff;
  width: 1000px;
  margin-top: 30.5px;
  position: absolute;
  top: 100%;
  right: 30px;
}

header::after {
  content: '';
  display: block;
  clear: both;
}

.site-title {
  max-width: 50%;
  
  margin: 0 30px 0 30px;
  font-size: 4.8rem;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
}


}

@media (max-width: 740px) {
  header {
      padding-bottom: 15px;
  }
  
  .site-search,
  .site-title {
    position: static;
    transform: translateY(0);
    display: block;
    max-width: 100%;
  }
  

}





.form-control {
  padding: 5px 4px 4px;
  border: 2px solid #cec4c4;
}

.form-control + .button {
  padding: 5px 4px 4px;
  margin: 0;
}
.container {
  margin-top: 30px;
  
  width: 100%;
}

.navbar {
  background-color:#606eb2;
  width: 20%;
  
}

.content {
  width: 105%;
}

ul {
  margin: 0;
  padding: 0;
}

li {
  list-style: none;
}

a {
  display: block;
  height: 40px;
  line-height: 40px;
  
  color: #FFFFFF;
  
  text-decoration: none;
  
  text-align: center;
}

a:hover {
  background-color: # ;
}

.nav-item {
  position: relative;
}





</style>