<?php
session_start();
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <link href="https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css" rel="stylesheet">
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Buy IT!</title>
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
</body>
</html>