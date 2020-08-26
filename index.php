<?php
session_start();
?>
<!DOCTYPE html>
<html>

<head>
  <link href="https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css" rel="stylesheet">
  <title>Buy IT!</title>

  <style>
    .textDesc {
      overflow: hidden;
      text-overflow: ellipsis;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      /* number of lines to show */
      -webkit-box-orient: vertical;
    }
  </style>
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
        <a href="" class="mr-5 hover:text-gray-900">About</a>
        <a href="" class="mr-5 hover:text-gray-900">Contact Us</a>
        <a href="" class="mr-5 hover:text-gray-900">Our Team</a>
      </nav>
      <?php
      try{
        if(session_status() == PHP_SESSION_ACTIVE ){
          $servername = "localhost";
          $username = "root";
          $password = "";
          $database = "buy_it";
          $id = "";
          if(isset($_SESSION['id'])){
            $id= $_SESSION['id'];
          // Create connection
            $connection = mysqli_connect($servername, $username, $password,$database);
            $query = "SELECT * FROM `user` WHERE `id`='$id'";
            $result = mysqli_query($connection, $query);
            $row = mysqli_fetch_assoc($result);
            if(mysqli_num_rows($result) !== 0)
              echo $row['full_name'];
          }
          }
          
      }

      catch(Exception $e){

      }
      
        
      ?>
      <a href =
      <?php if(isset($_SESSION['id'])){
        echo "logout.php";
      }else{
        echo "Login.php";
      }?>
       > <?php if(isset($_SESSION['id'])){
        echo " | Logout";
      }else{
        echo 'Login';
      }?></a>
    </div>
  </header>
  <section class="text-gray-700 body-font">
    <div class="container px-5 py-24 mx-auto">
      <div class="flex lg:w-2/3 w-full sm:flex-row flex-col mx-auto px-8 sm:px-0">
        <form action="" method="get" style="display:contents;">
          <input name="s" class="flex-grow w-full bg-gray-100 rounded border border-gray-400 focus:outline-none focus:border-indigo-500 text-base px-4 py-2 mr-4 mb-4 sm:mb-0" placeholder="Audi, Bmw, Auckland...." type="text">
          <button class="text-white bg-indigo-500 border-0 py-2 px-8 focus:outline-none hover:bg-indigo-600 rounded text-lg">Search</button>
        </form>
      </div>
    </div>
  </section>
  <section class="text-gray-700 body-font">
    <div class="container px-5 py-24 mx-auto">
      <div class="flex flex-wrap -m-4">
        <?php
        $testC = "";
        $servername = "localhost";
        $username = "root";
        $password = "";
        $database = "buy_it";
        // Create connection
        $connection = mysqli_connect($servername, $username, $password,$database);
        if (isset($_GET['s']) && $_GET['s'] != "") {
          $s = $_GET['s'];
          $testC = "WHERE product_name like '%$s%' or product_desc like '%$s%' or product_location like '%$s%'";
        }
          
          $query = "SELECT * FROM `product_data` $testC";
          $result = mysqli_query($connection, $query);
          if (mysqli_num_rows($result) > 0) {
            while ($rows = mysqli_fetch_assoc($result)) {
              ?>  
              <div class="lg:w-1/4 md:w-1/2 p-4 w-full">
                <a target="_blank" href="<?php echo $rows['item_url']; ?>" class="block relative h-48 rounded overflow-hidden">
                  <img alt="ecommerce" class="object-cover object-center w-full h-full block" src="<?php echo $rows['poduct_img']; ?>">
                </a>
                <div class="mt-4">
                  <h3 class="text-gray-500 text-xs tracking-widest title-font mb-1"><?php echo $rows['product_location']; ?></h3>
                  <h2 class="text-gray-900 title-font text-lg font-medium"><?php echo $rows['product_name']; ?></h2>
                  <p class="leading-relaxed mb-3 textDesc"><?php echo $rows['product_desc']; ?></p>
                  <p class="mt-1"><?php echo $rows['product_price']; ?></p>
                  <div class="flex items-center flex-wrap ">
                    <a target="_blank" href="<?php echo $rows['item_url']; ?>" class="text-indigo-500 inline-flex items-center md:mb-2 lg:mb-0">Learn More
                      <svg class="w-4 h-4 ml-2" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M5 12h14"></path>
                        <path d="M12 5l7 7-7 7"></path>
                      </svg>
                    </a>
                  </div>
                </div>
              </div>

            <?php
                }
              } else {
                ?>
            <div class="flex flex-col text-center w-full mb-20">
              <p class="lg:w-2/3 mx-auto leading-relaxed text-base">Nothing found.</p>
            </div>
        <?php
          }
        
        ?>

      </div>
    </div>
  </section>
  <footer class="text-gray-700 body-font">
    <div class="container px-5 py-8 mx-auto flex items-center sm:flex-row flex-col">
      <a class="flex title-font font-medium items-center md:justify-start justify-center text-gray-900">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-10 h-10 text-white p-2 bg-green-500 rounded-full" viewBox="0 0 24 24">
          <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"></path>
        </svg>
        <span class="ml-3 text-xl">Buy IT!</span>
      </a>
      <p class="text-sm text-gray-500 sm:ml-4 sm:pl-4 sm:border-l-2 sm:border-gray-200 sm:py-2 sm:mt-0 mt-4">© 2020 tailblocks —
        <a href="https://twitter.com/knyttneve" class="text-gray-600 ml-1" rel="noopener noreferrer" target="_blank">@knyttneve</a>
      </p>
      <span class="inline-flex sm:ml-auto sm:mt-0 mt-4 justify-center sm:justify-start">
        <a class="text-gray-500">
          <svg fill="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
            <path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z"></path>
          </svg>
        </a>
        <a class="ml-3 text-gray-500">
          <svg fill="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
            <path d="M23 3a10.9 10.9 0 01-3.14 1.53 4.48 4.48 0 00-7.86 3v1A10.66 10.66 0 013 4s-4 9 5 13a11.64 11.64 0 01-7 2c9 5 20 0 20-11.5a4.5 4.5 0 00-.08-.83A7.72 7.72 0 0023 3z"></path>
          </svg>
        </a>
        <a class="ml-3 text-gray-500">
          <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
            <rect width="20" height="20" x="2" y="2" rx="5" ry="5"></rect>
            <path d="M16 11.37A4 4 0 1112.63 8 4 4 0 0116 11.37zm1.5-4.87h.01"></path>
          </svg>
        </a>
        <a class="ml-3 text-gray-500">
          <svg fill="currentColor" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" class="w-5 h-5" viewBox="0 0 24 24">
            <path stroke="none" d="M16 8a6 6 0 016 6v7h-4v-7a2 2 0 00-2-2 2 2 0 00-2 2v7h-4v-7a6 6 0 016-6zM2 9h4v12H2z"></path>
            <circle cx="4" cy="4" r="2" stroke="none"></circle>
          </svg>
        </a>
      </span>
    </div>
  </footer>
  </body>

</html>