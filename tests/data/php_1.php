<?php

echo "this shouldn't be {$_('parsed')}";

$blue =<<<BLUE
This should get {$_('blue')}
BLUE

?>
None of this should be {$_('parsed either')}
<?php

echo <<<TEST
But this part should be parsed, such as {$_('red')}
and {$_('green')}
TEST
?>
