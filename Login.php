<?php
session_start();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link href="https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css" rel="stylesheet">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<header class="text-gray-700 body-font">
    <div class="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
      <a class="flex title-font font-medium items-center text-gray-900 mb-4 md:mb-0">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-10 h-10 text-white p-2 bg-green-500 rounded-full" viewBox="0 0 24 24">
          <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"></path>
        </svg>
        <span class="ml-3 text-xl">Buy IT!</span>
      </a>
      <nav class="md:ml-auto md:mr-auto flex flex-wrap items-center text-base justify-center">
        <a href="index.php" class="mr-5 hover:text-gray-900">Home</a>
        <a href="about.php" class="mr-5 hover:text-gray-900">About</a>
        <a href="contact_us.php" class="mr-5 hover:text-gray-900">Contact Us</a>
        <a href="ourteam.php" class="mr-5 hover:text-gray-900">Our Team</a>
      </nav>
      </div>
  </header>
<div>
    <?php 
        $servername = "localhost";
        $username = "root";
        $password = "";
        $database = "buy_it";
        // Create connection
        $connection = mysqli_connect($servername, $username, $password,$database);
        // echo $query;
        if(isset($_POST['create'])){
          $email = $_POST['email'];
          $password = $_POST['password'];
          $query = "SELECT id FROM `user` WHERE `user_email`='$email'";
          $result = mysqli_query($connection, $query);
          echo $query;
          if (mysqli_num_rows($result) == 1) {
            $query = "SELECT * FROM `user` WHERE `user_email`='$email'";
            $result = mysqli_query($connection, $query);
            $row = mysqli_fetch_assoc($result);
            if($row['use_passwrod'] == $password){
              $_SESSION['id'] = $row['id'];
              header("location: index.php");
            }else{
              echo "Invalid email or password.";  
            }
          }else{
            echo "Invalid email or password.";
          }
          }
    ?>
</div>


<section class="text-gray-700 body-font">
    <div class="container px-5 py-24 mx-auto flex flex-wrap items-center">
      <div class="lg:w-3/5 md:w-1/2 md:pr-16 lg:pr-0 pr-0">
        <h1 class="title-font font-medium text-3xl text-gray-900">Slow-carb next level shoindcgoitch ethical authentic, poko scenester</h1>
        <p class="leading-relaxed mt-4">Poke slow-carb mixtape knausgaard, typewriter street art gentrify hammock starladder roathse. Craies vegan tousled etsy austin.</p>
      </div>
      <div class="lg:w-2/6 md:w-1/2 bg-gray-200 rounded-lg p-8 flex flex-col md:ml-auto w-full mt-10 md:mt-0">
        <h2 class="text-gray-900 text-lg font-medium title-font mb-5">Sign In</h2>
        <form action="Login.php" method="post">
          <input class="bg-white rounded border border-gray-400 focus:outline-none focus:border-indigo-500 text-base px-4 py-2 mb-4" placeholder="Email" type="email" required name = 'email' > 
          <input class="bg-white rounded border border-gray-400 focus:outline-none focus:border-indigo-500 text-base px-4 py-2 mb-4" placeholder="Password" type="password" required name = 'password'>
          <input class="text-white bg-indigo-500 border-0 py-2 px-8 focus:outline-none hover:bg-indigo-600 rounded text-lg" placeholder = 'Sign In' name = 'create' type = 'submit'>
          <p class="text-xs text-gray-500 mt-3">Literally you probably haven't heard of them jean shorts.</p>
        </form>
        
      </div>
    </div>
  </section>
    
</body>
</html>