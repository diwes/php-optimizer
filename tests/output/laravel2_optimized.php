
<?php

$a = "1";

Route::get('/', function() { return view('welcome'); });

Route::get('/a', function() { return view('welcome'); });

Route::post('/b', function() { return view('welcome'); });

?>
