<link rel="stylesheet" type="text/css" href="panel2.css">
<link rel="stylesheet" type="text/css" href="user.css">
<header>
  <h1 class="site-title">
    Admin Panel
  </h1>
  

  
  <div class="card">
    <?php
$db_host = 'localhost'; // Server Name
$db_user = 'root'; // Username
$db_pass = ''; // Password
$db_name = 'trial'; // Database Name

$conn = mysqli_connect($db_host, $db_user, $db_pass, $db_name);
if (!$conn) {
  die ('Failed to connect to MySQL: ' . mysqli_connect_error());  
}

$sql = 'SELECT * 
    FROM registration';
$query = mysqli_query($conn, $sql);

if (!$query) {
  die ('SQL Error: ' . mysqli_error($conn));
}

  // delete task
  if (isset($_GET['del_task'])) {
    $id = $_GET['del_task'];

    mysqli_query($db, "DELETE FROM tasks WHERE id=".$id);
    header('location: index.php');
  }


?>


  <h1>Registered Users</h1>
  <br>
  <table class="data-table">

    <thead>
      <tr>

        <th>BRIDE NAME</th>
        <th>GROOM NAME</th>
        <th>EMAIL</th>
        <th>PHONE NO.</th>
        <th>USER</th>
        <th>PASS</th>



      </tr>
    </thead>
    <tbody>
    <?php

    while ($row = mysqli_fetch_array($query))
    {
        
      echo '<tr>
               
          <td>'.$row['bname'].'</td>
          <td>'.$row['gname'].'</td>
          <td>'.$row['num'].'</td>
          <td>'.$row['email'].'</td>
          <td>'.$row['uname'].'</td>
          <td>'.$row['pwd'].'</td>
          
        </tr>';

    }?>
    </tbody>

  </table>
 

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
  /***********************************************BOX********************************************************/
.card {
  background: #606eb2;
  border-radius: 2px;
  display: inline-block;
  height: 400px;
  margin: 1rem;
  position: relative;
  width: 300px;
  margin-left: 50px;

}
/******************************************TABLE********************************************************************/
 table {
      margin: auto;
      font-family: "Lucida Sans Unicode", "Lucida Grande", "Segoe Ui";
      font-size: 12px;
    }

    h1 {
      margin: 25px auto 0;
      text-align: center;
      text-transform: uppercase;
      font-size: 17px;
    }

    table td {
      transition: all .5s;
    }
    
    /* Table */
    .data-table {
      border-collapse: collapse;
      font-size: 14px;
      min-width: 437px;
    }

    .data-table th, 
    .data-table td {
      border: 1px solid #e1edff;
      padding: 7px 17px;
    }
    .data-table caption {
      margin: 7px;
    }

    /* Table Header */
    .data-table thead th {
      background-color: #508abb;
      color: #FFFFFF;
      border-color: #6ea1cc !important;
      text-transform: uppercase;
    }

    /* Table Body */
    .data-table tbody td {
      color: #353535;
    }
    .data-table tbody td:first-child,
    .data-table tbody td:nth-child(4),
    .data-table tbody td:last-child {
      text-align: right;
    }

    .data-table tbody tr:nth-child(odd) td {
      background-color: #f4fbff;
    }
    .data-table tbody tr:hover td {
      background-color: #ffffa2;
      border-color: #ffff0f;
    }

    /* Table Footer */
    .data-table tfoot th {
      background-color: #e5f5ff;
      text-align: right;
    }
    .data-table tfoot th:first-child {
      text-align: left;
    }
    .data-table tbody td:empty
    {
      background-color: #ffcccc;
    }




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