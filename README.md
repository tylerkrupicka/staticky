<h1>Staticky</h1>
<p>
A simple static site builder written in Python. Create layouts to be populated with posts, content, and variables easily--using standard html and css. Take any site template and populate content quickly.</p>

<h2>Setup</h2>
<p>Staticky has an automated setup command that will create the necessary directories and files to get started. Just place staticky.py in to an empty directory (or near empty) and run the script. It will ask you if you want to setup, and then create all the necessary base files and directories.</p>

<h2>Layouts</h2>
<p>The layouts folder is where all new pages are placed; any files in there will be propigated when the site is generated. All elements in the elements folder will be inserted in to layouts. For example: if you create a navbar.html file in the elements folder, this code will be placed everywhere you place [[navbar]] in the layouts.</p>

<h2>Config</h2>
<p>The config files allows you to define site-wide variables. Any created variables will be replaced in layouts where [[variable_name]] is found.</p>

<h2>Demo</h2>
<p>There is a demo branch of this repository that contains a simple website tutorial on basic features. Feel free to download it as an example, however the staticky.py in that branch might not be the most recent version. Make sure to use the staticky.py from the master branch.</p>

<p>Enjoy.</p>


