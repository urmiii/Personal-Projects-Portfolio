<!DOCTYPE html>
  <html>
  <head>

</head>
    
   
  <body>
    <div>
		<?php include 'header2.php';?>
		<br><br><br>  <br><br><br>  
  <h1 class="head">Your Vendor Team</h1>
  <style type="text/css">



  /*************************************************FLEXBOX************************************************************/
  .flex-container {
    display: flex;
    flex-wrap: nowrap;

  }

  .flex-container > div {
    background-color: #f1f1f1;
    width: 20px;
    margin: 20px;
    text-align: center;
    line-height: 180px;
    font-size: 30px;
    flex-grow: 8;
  }
  .a:hover{
    transform: scale(0.8);
  }
  .b:hover{
    transform: scale(0.8);
  }
  .c:hover{
    transform: scale(0.8);
  }
  /*************************************************TODOLIST************************************************************/

  form {
    width: 800px;

  }
  input {
    width: 1400px;
    height: 60px;
    background: none;
    border: none;
    border-bottom: 1px solid #1111;
    outline: none;
    font: 300 28px 'Ubuntu', sans-serif;
    padding: 20px;
  }
  form p {
    color: red;

  }

  #add_btn {
    background-color: #333333;
    border: 2px solid #ECF3F3;
    border-radius: 27px;
    color: white;
    cursor: pointer;
    font-size: 20px;

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
      width: 100%;


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
  button{
    background-color: #333333;
    border: 2px solid #ECF3F3;
    border-radius: 27px;
    color: white;
    cursor: pointer;
    font-size: 12px;
    margin-top: 20px;
    padding: 10px 12px;
    text-transform: uppercase;
    transition: all 200ms;

  }
    button:hover, button:focus{
      background-color: #ECF3F3;
      color: #333333;
      outline: 0;}

.guest{
      background-color: #333333;
    border: 2px solid #ECF3F3;
    border-radius: 27px;
    color: white;
    cursor: pointer;
    font-size: 12px;
    margin-top: 20px;
    padding: 10px 12px;
    text-transform: uppercase;
    transition: all 200ms;

}
    .guest:hover, .guest:focus{
      background-color: #ECF3F3;
      color: #333333;
      outline: 0;}
  </style>


<div>


  <div class="flex-container">
    <div class="a" style="font-size: 18px;">Your Vendor Details:<p id="demo" style="font-size:18px;"></p></div>
    <div class="b" style="font-size: 18px;">Your Photographer Details:<p id="demo_2" style="font-size: 18px;"></p></div>
    <div class="c" style="font-size: 18px;">Your Band Details:<p id="demo_3" style="font-size: 18px;"></p></div>  

  </div>
    &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<button class="vendor_btn" onclick="myFunction()">Add Venue details</button>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
  <button class="vendor_btn" onclick="myFunction_2()">Add Photogrpahy details</button>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
    <button class="vendor_btn" onclick="myFunction_3()">Add Band details</button>
  <script>
  function myFunction() {
    var txt;
    var person = prompt("Please enter location:", "");


    if (person == null || person == "" ) {
      txt = "";
    } else {
      txt = "Venue added:" + person;

    }
    document.getElementById("demo").innerHTML = txt;
  }
  function myFunction_2() {
    var txt;
    var photographer = prompt("Please enter  name:", "");

    if (photographer == null || photographer == ""  ) {
      txt = "User cancelled the prompt.";
    } else {
      txt = "photographer added:" + photographer;

    }
    document.getElementById("demo_2").innerHTML = txt;
  }
  function myFunction_3() {
    var txt;
    var name = prompt("Please enter  bandname:", "");

    if (name == null || name == "" ) {
      txt = "User cancelled the prompt.";
    } else {
      txt = "band added:" + name;

    }
    document.getElementById("demo_3").innerHTML = txt;
  }
  </script>
  <br><br><br><br>

  <?php 
    
    $errors = "";

    // connect to database
    $db = mysqli_connect("localhost", "root", "", "todo");

    // insert a quote if submit button is clicked
    if (isset($_POST['submit'])) {

      if (empty($_POST['task'])) {
        $errors = "You must fill in the task";
      }else{
        $task = $_POST['task'];
        $query = "INSERT INTO tasks (task) VALUES ('$task')";
        mysqli_query($db, $query);
        header('location: tools.php');
      }
    } 

    // delete task
    if (isset($_GET['del_task'])) {
      $id = $_GET['del_task'];

      mysqli_query($db, "DELETE FROM tasks WHERE id=".$id);
      header('location: tools.php');
    }

    // select all tasks if page is visited or refreshed
    $tasks = mysqli_query($db, "SELECT * FROM tasks");

  ?>


  <h1 class="head">Upcoming Tasks</h1>
    <form method="post" action="tools.php" class="input_form">
      <?php if (isset($errors)) { ?>
        <p><?php echo $errors; ?></p>
      <?php } ?>
      <input type="text" name="task" class="app-insert" placeholder="Insert here...">
  <button type="submit" name="submit" id="add_btn" class="btn" >
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
            <td class="task"> <?php echo $row['task']; ?> </td>
            <td class="delete"> 
              <a href="tools.php?del_task=<?php echo $row['id'] ?>">delete</a> 
            </td>
          </tr>
        <?php $i++; } ?>  
      </tbody>
    </table>


  <h1 class="head">Guest List</h1>
  <div class="flex-container">
    <div class="a" style="font-size: 10px;"><a class="guest" href="Guestlist.php" style="color: white;">Add Guestlist</a></div>
    <div class="b" style="font-size: 18px;"><button onclick="myFunction_4()">Add/Update Budget</button><p id="demo_4"></p></div>
  </div> 
  <script type="text/javascript">
    function myFunction_4() {
    var txt;
    var name = prompt("Please enter  your budget:", "");
   
    
    if (name == null || name == "" ) {
      txt = "";
    } else {
      txt = "Budget added:" + name;

    }
    document.getElementById("demo_4").innerHTML = txt;
  }
  </script>
  <style type="text/css">
    .boxmodel{
    background-color: #f1f1f1;
    width: 1290px;
    padding: 25px;
    margin: 25px;
    height: 100px;

    }
  #slct{
    background-color: #333333;
    border: 2px solid #ECF3F3;
    border-radius: 27px;
    color: white;
    cursor: pointer;
    font-size: 12px;
    margin-top: 20px;
    padding: 5px 5px;
  }
    #slct:hover, #slct:focus{
      background-color: #ECF3F3;
      color: #333333;
      outline: 0;}

  </style>
  <h1 class="head">Wedding Details</h1>
  <div class="boxmodel">
    <br>
  <div style="  font-size: 20px;" class="custom-select">
    Color:
    <select id="slct" style="  font-size: 16px; border-radius: 15px;">
      <option>Red</option>
      <option>Black</option>
      <option>White</option>
    </select>
           &nbsp&nbsp&nbsp &nbsp&nbsp&nbsp &nbsp&nbsp&nbsp &nbsp&nbsp&nbsp &nbsp&nbsp&nbsp &nbsp&nbsp&nbsp 
    Season:
    <select id="slct" style="  font-size: 16px;">
      <option>Winter</option>
      <option>Summer</option>
      <option>Monsoon</option>
    </select>
                 &nbsp&nbsp&nbsp &nbsp&nbsp&nbsp &nbsp&nbsp&nbsp &nbsp&nbsp&nbsp &nbsp&nbsp&nbsp &nbsp&nbsp&nbsp 
    Style:
    <select id="slct" style="  font-size: 16px;">
      <option>Beach</option>
      <option>Casual</option>
      <option>Classic</option>
    </select>
                  &nbsp&nbsp&nbsp &nbsp&nbsp&nbsp &nbsp&nbsp&nbsp &nbsp&nbsp&nbsp &nbsp&nbsp&nbsp &nbsp&nbsp&nbsp 
    Dress:
    <select id="slct" style="  font-size: 16px;">
      <option>Silhouette</option>
      <option>Casual</option>
      <option>Classic</option>
    </select>
             &nbsp&nbsp&nbsp &nbsp&nbsp&nbsp &nbsp&nbsp&nbsp &nbsp&nbsp&nbsp &nbsp&nbsp&nbsp 
  Wedding:
    <select id="slct" style="  font-size: 16px;">
      <option>Destination</option>
      <option>Court</option>
      <option>Classic</option>
    </select>
  </div>
  </div>
</div>
</div>
  </body>
  </html>