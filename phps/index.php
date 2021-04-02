<?PHP
  use \DirectoryIterator;

  function getFileList($dir)
  {
    // array to hold return value
    $retval = [];

    // add trailing slash if missing
    if(substr($dir, -1) != "/") $dir .= "/";

    // open directory for reading
    $d = new DirectoryIterator($dir) or die("getFileList: Failed opening directory $dir for reading");
    foreach($d as $fileinfo) {
      // skip hidden files
      if($fileinfo->isDot()) continue;
      $retval[] = [
        'name' => "{$dir}{$fileinfo}",
        'type' => ($fileinfo->getType() == "dir") ? "dir" : mime_content_type($fileinfo->getRealPath()),
        'size' => $fileinfo->getSize(),
        'lastmod' => $fileinfo->getMTime()
      ];
    }

    return $retval;
  }

  $dirlist = getFileList("./");

?>