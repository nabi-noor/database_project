<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css" rel="stylesheet">
    <title>Document</title>
</head>
<body>
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
          $fullname = $_POST['fullname'];
          $email = $_POST['email'];
          $password = $_POST['password'];
          $query = "SELECT id FROM `user` WHERE `user_email`='$email'";
          $result = mysqli_query($connection, $query);
          echo $query;
          if (mysqli_num_rows($result) == 0) {
            $query = "INSERT INTO `user` (full_name,user_email,use_passwrod) VALUES('$fullname','$email','$password')";
            $result = mysqli_query($connection, $query);
            header("location: Login.php");   
          }else{
            echo "The email already exits try signing up with a different one.";
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
          <form action="Signup.php" method="post">
            <h2 class="text-gray-900 text-lg font-medium title-font mb-5">Sign Up</h2>
            <input class="bg-white rounded border border-gray-400 focus:outline-none focus:border-indigo-500 text-base px-4 py-2 mb-4" placeholder="Full Name" type="text" name="fullname" required>
            <input class="bg-white rounded border border-gray-400 focus:outline-none focus:border-indigo-500 text-base px-4 py-2 mb-4" placeholder="Email" type="email" name="email" required>
            <input class="bg-white rounded border border-gray-400 focus:outline-none focus:border-indigo-500 text-base px-4 py-2 mb-4" placeholder="Password" type="password" name="password" required>
            <br>
            <input class="text-white bg-indigo-500 border-0 py-2 px-8 focus:outline-none hover:bg-indigo-600 rounded text-lg" type="submit" name="create" value="Sign Up">
            <p class="text-xs text-gray-500 mt-3">Literally you probably haven't heard of them jean shorts.</p>
          </form>
        </div>
      </div>
    </section>
</body>
</html>