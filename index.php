<?php
# echo "\n OLÁ,EU SOU O BOT DE ATENDIMENTO! \n ";

$servidor = 'localhost';
$usuario = 'root';
$senha = '';
$banco = 'bot_curso';
$conn = mysqli_connect($servidor, $usuario, $senha, $banco);

if (!$conn) {
    #echo "\n Conexão concluida!";
} else {
    echo "\n Conexão não concuida ". mysqli_error($conn);
}

$nome = "victor";
$telefone = "123456";

$sql = "INSERT INTO bot (nome, telefone) VALUES ('$nome', '$telefone')";

$query = mysqli_query($conn, $sql);

if (!$query) {
    echo " \n erro ao inserir os dados:\n  " . mysqli_error($conn);
} else {
# echo "\n deu tudo certo\n ";
}
###########################
#VARIAVEIS IMPORTANTES 
$numero_telefone = $_GET['telefone'];
$msg = $_GET['msg'];
$usuario = $_GET ['usuario'];
echo "*telefone* $numero_telefone *MSG* $msg *usuario* $usuario";
?>