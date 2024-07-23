import streamlit as st

# Lista de queijarias com informações adicionais
queijarias = [
    {
        "nome": "A Queijaria",
        "endereco": "R. Aspicuelta, 35, V. Madalena",
        "telefone": "3812-6449",
        "cidade": "São Paulo",
        "link": "http://www.aqueijaria.com.br/"
    },
    {
        "nome": "Armazém do Mineiro",
        "endereco": "R. Azevedo Soares, 1.653, V. Gomes Cardim",
        "telefone": "2309-4847",
        "cidade": "São Paulo",
        "link": "https://www.armazemdomineiro.com.br/"
    },
    {
        "nome": "Armazém São Paulo",
        "endereco": "R. Pedro Cristi, 89, Pinheiros, box 11 e 12",
        "telefone": "3031-1012",
        "cidade": "São Paulo",
        "link": ""
    },
    {
        "nome": "À Mercê",
        "endereco": "Praça da República 119, Centro",
        "telefone": "(11) 91717-8684",
        "cidade": "São Paulo",
        "link": "https://www.instagram.com/amerce.sp/"
    },
    {
        "nome": "Casa Santa Luzia",
        "endereco": "Al. Lorena, 1.471, Jd. Paulista",
        "telefone": "3897-5000",
        "cidade": "São Paulo",
        "link": "http://www.santaluzia.com.br/"
    },
    {
        "nome": "Cave 381",
        "endereco": "Av. Mascote, 664, Vila Mascote",
        "telefone": "(11) 91208-9819",
        "cidade": "São Paulo",
        "link": "https://www.instagram.com/queijariacave381/"
    },
    {
        "nome": "Empório Sabor e Cia",
        "endereco": "R. Capote Valente, 386, Pinheiros",
        "telefone": "3064-8172",
        "cidade": "São Paulo",
        "link": "https://www.emporiosaborecia.com.br/"
    },
    {
        "nome": "Empório Santa Maria",
        "endereco": "Av. Cidade Jardim, 790, Itaim Bibi",
        "telefone": "3706-521",
        "cidade": "São Paulo",
        "link": "http://loja.emporiosantamaria.com.br/"
    },
    {
        "nome": "Galeria do Queijo",
        "endereco": "R. Gen. Chagas Santos, 815, lj. 6, Saúde",
        "telefone": "2639-9206",
        "cidade": "São Paulo",
        "link": "https://www.facebook.com/galeriadoqueijoimigrantes/"
    },
    {
        "nome": "Lá do Interior",
        "endereco": "Loja Online (atende capital e grande São Paulo)",
        "telefone": "(11) 96342-4457",
        "cidade": "São Paulo",
        "link": "https://ladointerior.com.br/"
    },
    {
        "nome": "Mestre Queijeiro",
        "endereco": "R. Simão Álvares, 112, Pinheiros",
        "telefone": "(11) 2369-1087",
        "cidade": "São Paulo",
        "link": "https://www.mestrequeijeiro.com.br/"
    },
    {
        "nome": "Preciosa Curadoria",
        "endereco": "R. das Camélias, 21, Mirandópolis",
        "telefone": "(11) 98721-2855",
        "cidade": "São Paulo",
        "link": "https://www.instagram.com/preciosacuradoria/"
    },
    {
        "nome": "Queijuz",
        "endereco": "Av. Ipiranga, 200, loja 28 (Edifício Copan), República",
        "telefone": "(11) 3231-4988",
        "cidade": "São Paulo",
        "link": "https://www.instagram.com/queijuz/"
    },
    {
        "nome": "Quitanda",
        "endereco": "R. Mateus Grou, 159, Pinheiros",
        "telefone": "(11) 3060-3230",
        "cidade": "São Paulo",
        "link": "http://www.quitanda.com/"
    },
    {
        "nome": "Sabores de Queijo",
        "endereco": "Trav. Dr. Leopoldo, 56, Itaim Bibi",
        "telefone": "(11) 99458-7915",
        "cidade": "São Paulo",
        "link": "https://www.instagram.com/saboresdequeijosp_/"
    },
    {
        "nome": "O Mió do Queijo",
        "endereco": "Rua Tuiuti, 1065 - Sala 8",
        "telefone": "(19) 3406-3435",
        "cidade": "Americana",
        "link": "https://www.omiodoqueijo.com.br"
    },
    {
        "nome": "Teta Cheese Bar",
        "endereco": "CLS 103, Bloco B, Loja 34",
        "telefone": "(61) 3554-6970",
        "cidade": "Brasília",
        "link": "https://tetabar.com.br/"
    },
    {
        "nome": "Empório Santo João",
        "endereco": "Praça Alfredo Cardoso, 1336 - Box 4",
        "telefone": "(19) 99708-7700",
        "cidade": "Piracicaba",
        "link": "http://www.emporiosantojoao.com.br"
    },
    {
        "nome": "Casa Vivá",
        "endereco": "Rua Dinarte Ribeiro, 128",
        "telefone": "(51) 3072-7028",
        "cidade": "Porto Alegre",
        "link": "https://casavivaqueijosevinhos.com.br"
    },
    {
        "nome": "Queijaria do Chico",
        "endereco": "Rua Jorge Tibiriçá, 3582",
        "telefone": "(17) 3235-1386 / (11) 97647-4263",
        "cidade": "São José do Rio Preto",
        "link": "https://queijaria-do-chico.negocio.site/"
    },
    {
        "nome": "Cave Queijos",
        "endereco": "R. das Dálias, 37",
        "telefone": "(71) 98884-7496 / (71) 98243-5411",
        "cidade": "Salvador",
        "link": "https://www.instagram.com/cavequeijos/"
    },
    {
        "nome": "Lá do Interior",
        "endereco": "Loja Online (atende Socorro e grande São Paulo)",
        "telefone": "(11) 96342-4457",
        "cidade": "Socorro",
        "link": "https://ladointerior.com.br/"
    },
    {
        "nome": "Cadim",
        "endereco": "Loja online (atende Vale do Paraíba e São Paulo)",
        "telefone": "(12) 99675-7387",
        "cidade": "Vale do Paraíba",
        "link": "https://www.instagram.com/queijoscadim/"
    },
    {
        "nome": "Tábua das Rosas",
        "endereco": "Rua das Rosas, 753 - Mirandópolis - São Paulo - SP",
        "telefone": "(11) 91874-3017",
        "cidade": "São Paulo",
        "link": "https://www.instagram.com/tabuadasrosas/"
    },
    {
        "nome": "Instituto Chão",
        "endereco": "R. Harmonia, 114, Vila Madalena, São Paulo SP",
        "telefone": "(11) 3819-4205",
        "cidade": "São Paulo",
        "link": "https://www.instagram.com/institutochao/"
    },
]

# Função para exibir uma queijaria
def exibir_queijaria(queijaria):
    st.markdown(f"""
    <div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px; margin: 10px 0;">
        <h3><a href="{queijaria['link']}" target="_blank" style="text-decoration: none; color: #007BFF;">{queijaria['nome']}</a></h3>
        <p><strong>Endereço:</strong> {queijaria['endereco']}</p>
        <p><strong>Telefone:</strong> {queijaria['telefone']}</p>
    </div>
    """, unsafe_allow_html=True)

# Título da página
st.markdown("<h1 style='text-align: center; color: #333;'>Onde comprar queijo artesanal no Brasil</h1>", unsafe_allow_html=True)

# Exibir lista de queijarias por cidade
cidades = list(set(q["cidade"] for q in queijarias))
cidades.insert(0, "Todos")  # Adicionar opção "Todos" no início da lista
cidade_selecionada = st.selectbox("Selecione a cidade", cidades)

# Filtrar queijarias pela cidade selecionada
if cidade_selecionada == "Todos":
    queijarias_filtradas = queijarias
else:
    queijarias_filtradas = [q for q in queijarias if q["cidade"] == cidade_selecionada]

# Exibir as queijarias da cidade selecionada
for queijaria in queijarias_filtradas:
    exibir_queijaria(queijaria)
