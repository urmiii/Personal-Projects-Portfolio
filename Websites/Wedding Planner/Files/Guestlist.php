<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" type="text/css" href="guestlist.css">
</head>
<body>


<!-----------------------------------------------------NAVIGATION BAR----------------------------------------------------->
<?php include 'header2.php';?>

<!-----------------------------------------------------YOUR PROFILE----------------------------------------------------->



<?php 
  
  $errors = "";

  // connect to database
  $db = mysqli_connect("localhost", "root", "", "todo");

  // insert a quote if submit button is clicked
  if (isset($_POST['submit'])) {

    if (empty($_POST['task'])) {
      $errors = "You must fill in the name";
    }else{
      $task = $_POST['task'];
      $query = "INSERT INTO guest (name) VALUES ('$task')";
      mysqli_query($db, $query);
      header('location: Guestlist.php');
    }
  } 

  // delete task
  if (isset($_GET['del_task'])) {
    $id = $_GET['del_task'];

    mysqli_query($db, "DELETE FROM guest WHERE id=".$id);
    header('location: Guestlist.php');
  }

  // select all tasks if page is visited or refreshed
  $tasks = mysqli_query($db, "SELECT * FROM guest");

?>
<!DOCTYPE html>
<html>

<head>
<style type="text/css">
  

.heading{
  color: #6d6d6d;
  font-family: 'Cormorant Garamond';
  font-size: 23px;
  line-height: 72px;
  letter-spacing: 15.5px;
  text-align: left;
  padding-left: 0px;
  text-indent: 24px;
  margin-left: 17px;
  margin-top: 50px;
    border-bottom: 1px solid #bdc3c7;
 

}

form {
  width: 800px;
  margin: 50px auto 20px;
}
input {
  width: 80%;
  height: 60px;
  background: none;
  border: none;
  border-bottom: 1px solid #bdc3c7;
  outline: none;
  font: 300 28px 'Ubuntu', sans-serif;
  padding: 20px;
}
form p {
  color: red;
  margin: 0px;
}

#add_btn {
  background-color: #333333;
  border: 2px solid #ECF3F3;
  border-radius: 27px;
  color: white;
  cursor: pointer;
  font-size: 20px;
  border-bottom: 1px solid #bdc3c7;
  padding: 15px 30px;
  text-transform: uppercase;
  transition: all 200ms;
  background-color: #555555;
  height: 60px;
}
  #add_btn:hover, #add_btn:focus{
    background-color: #ECF3F3;
    color: #333333;
    outline: 0;}


table {
    width: 55%;
  width: 800px;
  margin: 0 auto;
}

tr {
  width: 100%;
  height: 60px;
  line-height: 60px;
  padding: 0 20px;
  position: relative;
  color: #333;
  font: 300 18px 'Ubuntu', sans-serif;
  transition: all .2s ease;
}

th {
  font-size: 29px;
  color: #7f8c8d;
}

th, td{
  border: none;
    height: 30px;
    padding: 2px;
}

tr:hover {
  background: rgba(0, 0, 0, .04);

}

.task {
  text-align: left;
}

.delete{
  text-align: center;
}
.delete a{
  color:  #333;
  background: rgba(0, 0, 0, .04);
  padding: 1px 6px;
  border-radius: 3px;
  text-decoration: none;
    font: 300 18px 'Ubuntu', sans-serif;

}
.delete a:hover{
      background-color: #ECF3F3;
    color: #333333;
    outline: 0;
}



</style>
</head>

<body>
<header>
  <!-----------------------------------------------------GROOM'S GUESTLIST------------------------------------------------------------->

  <div class="heading">
  <h2> &nbsp&nbspGuest List</h2>
  </div>
</header>

  <form method="post" action="" class="input_form">
    <?php if (isset($errors)) { ?>
      <p><?php echo $errors; ?></p>
    <?php } ?>
    <input type="text" name="task" class="app-insert" placeholder="Insert here...">
    <button type="submit" name="submit" id="add_btn" class="btn">
      Add </button>
  </form>


  <table>
    <thead>
      <tr class="listt">
        <th></th>
        <th class="gg"></th>
        <th style="width: 60px;"></th>
      </tr>
    </thead>

    <tbody>
      <?php $i = 1; while ($row = mysqli_fetch_array($tasks)) { ?>
        <tr>
          <td> <?php echo $i; ?> </td>
          <td class="task"> <?php echo $row['name']; ?> </td>
          <td class="delete"> 
            <a href="Guestlist.php?del_task=<?php echo $row['id'] ?>">delete</a> 
          </td>
        </tr>
      <?php $i++; } ?>  
    </tbody>
  </table>


</body>
</html>