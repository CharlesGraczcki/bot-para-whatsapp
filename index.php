<?php
echo "\n OLÁ,EU SOU O BOT DE ATENDIMENTO! \n ";

$servidor = 'localhost';
$usuario = 'root';
$senha = '';
$banco = 'bot';
$conn = mysqli_connect($servidor, $usuario, $senha, $banco);

if (!$conn) {
    echo "\n Conexão concluida!";
} else {
    echo "\n Conexão não concuida :/  ";
}

$nome = "victor";
$telefone = "123456";

$sql = "INSERT INTO bot (nome, telefone) VALUES ('$nome', '$telefone')";

$query = mysqli_query($conn, $sql);

if (!$query) {
    echo " \n erro ao inserir os dados:\n  " . mysqli_error($conn);
} else {
    echo "\n deu tudo certo\n ";
}
?>
<?php
$sql = "SELECT * FROM bot WHERE nome = 'victor'";
$query = mysqli_query($conn, $sql);

while ($row_usuarios = mysqli_fetch_array($query)) {
    $nome = $row_usuarios['nome'];
    echo $nome;
}
?>