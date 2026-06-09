// Memória do carrinho no Front-end
let carrinho = [];

async function carregarProdutos() {
    try {
        const resposta = await fetch('http://127.0.0.1:8000/produtos');
        const produtos = await resposta.json();
        
        const vitrine = document.getElementById('vitrine-produtos');
        vitrine.innerHTML = ''; 

        produtos.forEach(produto => {
            const card = document.createElement('div');
            card.className = 'produto-card';
            card.innerHTML = `
                <button class="btn-excluir" onclick="excluirProduto(${produto.id}, '${produto.nome}')" title="Excluir">
                    <i class="fa-solid fa-trash-can"></i>
                </button>
                
                <h3>${produto.nome}</h3>
                <p>R$ ${produto.preco.toFixed(2)}</p>
                <button class="btn-adicionar" onclick="adicionarAoCarrinho(${produto.id}, '${produto.nome}', ${produto.preco})">
                    Adicionar
                </button>
            `;
            vitrine.appendChild(card);
        });
    } catch (erro) {
        console.error(erro);
    }
}

// LÓGICA DO CARRINHO
function adicionarAoCarrinho(id, nome, preco) {
    const itemExistente = carrinho.find(item => item.produto_id === id);
    
    if (itemExistente) {
        itemExistente.quantidade += 1; 
    } else {
        carrinho.push({ produto_id: id, nome: nome, preco: preco, quantidade: 1 });
    }
    atualizarTelaCarrinho();
}

function atualizarTelaCarrinho() {
    const lista = document.getElementById('lista-carrinho');
    const totalElemento = document.getElementById('valor-total');
    
    lista.innerHTML = ''; 
    let total = 0;

    if (carrinho.length === 0) {
        lista.innerHTML = '<p style="color: #7f8c8d; font-size: 0.9rem;">O carrinho está vazio.</p>';
    } else {
        carrinho.forEach(item => {
            const subtotal = item.preco * item.quantidade;
            total += subtotal;
            lista.innerHTML += `
                <div class="item-carrinho">
                    <span>${item.quantidade}x ${item.nome}</span>
                    <span>R$ ${subtotal.toFixed(2)}</span>
                </div>
            `;
        });
    }
    totalElemento.innerText = `R$ ${total.toFixed(2)}`;
}

// COMUNICAÇÃO COM O SEU BACK-END (O POST)
async function finalizarCompra() {
    if (carrinho.length === 0) {
        mostrarNotificacao("Adicione itens ao carrinho antes de finalizar!", "warning");
        return;
    }

    const pacoteVenda = {
        itens: carrinho.map(item => ({
            produto_id: item.produto_id,
            quantidade: item.quantidade
        }))
    };

    try {
        const resposta = await fetch('http://127.0.0.1:8000/pedidos', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(pacoteVenda) 
        });

        if (resposta.ok) {
            const dados = await resposta.json();
            mostrarNotificacao(`${dados.mensagem}\nValor cobrado: R$ ${dados.total.toFixed(2)}`, "success");
            carrinho = []; 
            atualizarTelaCarrinho();
        } else {
            const erro = await resposta.json();
            mostrarNotificacao(`Erro: ${erro.detail}`, "error");
        }
    } catch (erro) {
        mostrarNotificacao("Erro de conexão com o servidor.", "error");
    }
}

// CADASTRO DE NOVOS PRODUTOS NO BACK-END
async function cadastrarProduto(event) {
    event.preventDefault(); 

    const nomeInput = document.getElementById('novo-nome').value;
    const precoInput = parseFloat(document.getElementById('novo-preco').value);

    const novoProduto = {
        nome: nomeInput,
        preco: precoInput
    };

    try {
        const resposta = await fetch('http://127.0.0.1:8000/produtos', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(novoProduto)
        });

        if (resposta.ok) {
            mostrarNotificacao(`Produto '${nomeInput}' cadastrado com sucesso!`, "success");
            document.getElementById('form-produto').reset(); 
            carregarProdutos(); 
        } else {
            mostrarNotificacao("Erro ao salvar o produto no banco de dados.", "error");
        }
    } catch (erro) {
        mostrarNotificacao("Erro de conexão com o servidor.", "error");
        console.error(erro);
    }
}

// ==========================================
// SISTEMA DE NOTIFICAÇÕES (TOAST)
// ==========================================
function mostrarNotificacao(mensagem, tipo = 'success') {
    const container = document.getElementById('toast-container');
    if (!container) return;

    const toast = document.createElement('div');
    toast.className = `toast ${tipo}`;
    
    // Define um ícone com base no tipo
    let icone = '📌';
    if (tipo === 'success') icone = '✅';
    if (tipo === 'error') icone = '❌';
    if (tipo === 'warning') icone = '⚠️';

    // O .replace transforma o \n do texto em quebra de linha real no HTML
    toast.innerHTML = `<span>${icone}</span> <div>${mensagem.replace('\n', '<br>')}</div>`;
    
    container.appendChild(toast);

    // Dispara a animação de entrada
    setTimeout(() => toast.classList.add('show'), 10);

    // Remove automaticamente após 4 segundos
    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => toast.remove(), 300); // Espera a animação de saída terminar para deletar o elemento
    }, 4000);
}

// ==========================================
// EXCLUIR PRODUTO (MODAL CUSTOMIZADO)
// ==========================================
let produtoParaExcluir = null; // Memória temporária

// 1. O botão da lixeira chama esta função para ABRIR o modal
function excluirProduto(id, nome) {
    produtoParaExcluir = { id, nome };
    document.getElementById('modal-nome-produto').innerText = nome;
    document.getElementById('modal-exclusao').classList.add('show');
}

// 2. O botão "Cancelar" chama esta função para FECHAR o modal
function fecharModal() {
    document.getElementById('modal-exclusao').classList.remove('show');
    produtoParaExcluir = null;
}

// 3. O botão vermelho do modal chama esta função para EXECUTAR a deleção
async function executarExclusao() {
    if (!produtoParaExcluir) return;
    const { id, nome } = produtoParaExcluir;

    try {
        const resposta = await fetch(`http://127.0.0.1:8000/produtos/${id}`, {
            method: 'DELETE'
        });

        if (resposta.ok) {
            mostrarNotificacao(`O produto '${nome}' foi retirado das vendas.`, "success");
            carregarProdutos(); 
        } else {
            const erro = await resposta.json();
            mostrarNotificacao(`Erro: ${erro.detail}`, "error");
        }
    } catch (erro) {
        mostrarNotificacao("Erro de conexão com o servidor.", "error");
    }
    
    // Fecha o modal no final, dando certo ou errado
    fecharModal(); 
}

// Inicializa o sistema
carregarProdutos();