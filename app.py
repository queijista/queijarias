import streamlit as st

# Lista de queijarias com informações adicionais
queijarias = [
    {
        "nome": "Armazém do Mineiro",
        "endereco": "R. Azevedo Soares, 1.653, V. Gomes Cardim",
        "telefone": "2309-4847",
        "cidade": "São Paulo SP",
        "link": "https://www.armazemdomineiro.com.br/"
    },
    {
        "nome": "Armazém São Paulo",
        "endereco": "R. Pedro Cristi, 89, Pinheiros, box 11 e 12",
        "telefone": "3031-1012",
        "cidade": "São Paulo SP",
        "link": ""
    },
    {
        "nome": "À Mercê",
        "endereco": "Praça da República 119, Centro",
        "telefone": "(11) 91717-8684",
        "cidade": "São Paulo SP",
        "link": "https://www.instagram.com/amerce.sp/"
    },
    {
        "nome": "Casa Santa Luzia",
        "endereco": "Al. Lorena, 1.471, Jd. Paulista",
        "telefone": "3897-5000",
        "cidade": "São Paulo SP",
        "link": "http://www.santaluzia.com.br/"
    },
    {
        "nome": "Cave 381",
        "endereco": "Av. Mascote, 664, Vila Mascote",
        "telefone": "(11) 91208-9819",
        "cidade": "São Paulo SP",
        "link": "https://www.instagram.com/queijariacave381/"
    },
    {
        "nome": "Empório Sabor e Cia",
        "endereco": "R. Capote Valente, 386, Pinheiros",
        "telefone": "3064-8172",
        "cidade": "São Paulo SP",
        "link": "https://www.emporiosaborecia.com.br/"
    },
    {
        "nome": "Empório Santa Maria",
        "endereco": "Av. Cidade Jardim, 790, Itaim Bibi",
        "telefone": "3706-521",
        "cidade": "São Paulo SP",
        "link": "http://loja.emporiosantamaria.com.br/"
    },
    {
        "nome": "Galeria do Queijo",
        "endereco": "R. Gen. Chagas Santos, 815, lj. 6, Saúde",
        "telefone": "2639-9206",
        "cidade": "São Paulo SP",
        "link": "https://www.facebook.com/galeriadoqueijoimigrantes/"
    },
    {
        "nome": "Lá do Interior",
        "endereco": "Loja Online (atende capital e grande São Paulo)",
        "telefone": "(11) 96342-4457",
        "cidade": "São Paulo SP",
        "link": "https://ladointerior.com.br/"
    },
    {
        "nome": "Mestre Queijeiro",
        "endereco": "R. Simão Álvares, 112, Pinheiros",
        "telefone": "(11) 2369-1087",
        "cidade": "São Paulo SP",
        "link": "https://www.mestrequeijeiro.com.br/"
    },
    {
        "nome": "Preciosa Curadoria",
        "endereco": "R. das Camélias, 21, Mirandópolis",
        "telefone": "(11) 98721-2855",
        "cidade": "São Paulo SP",
        "link": "https://www.instagram.com/preciosacuradoria/"
    },
    {
        "nome": "Queijuz",
        "endereco": "Av. Ipiranga, 200, loja 28 (Edifício Copan), República",
        "telefone": "(11) 3231-4988",
        "cidade": "São Paulo SP",
        "link": "https://www.instagram.com/queijuz/"
    },
    {
        "nome": "Quitanda",
        "endereco": "R. Mateus Grou, 159, Pinheiros",
        "telefone": "(11) 3060-3230",
        "cidade": "São Paulo SP",
        "link": "http://www.quitanda.com/"
    },
    {
        "nome": "Sabores de Queijo",
        "endereco": "Trav. Dr. Leopoldo, 56, Itaim Bibi",
        "telefone": "(11) 99458-7915",
        "cidade": "São Paulo SP",
        "link": "https://www.instagram.com/saboresdequeijosp_/"
    },
    {
        "nome": "O Mió do Queijo",
        "endereco": "Rua Tuiuti, 1065 - Sala 8",
        "telefone": "(19) 3406-3435",
        "cidade": "Americana SP",
        "link": "https://www.omiodoqueijo.com.br"
    },
    {
        "nome": "Teta Cheese Bar",
        "endereco": "CLS 103, Bloco B, Loja 34",
        "telefone": "(61) 3554-6970",
        "cidade": "Brasília DF",
        "link": "https://tetabar.com.br/"
    },
    {
        "nome": "Empório Santo João",
        "endereco": "Praça Alfredo Cardoso, 1336 - Box 4",
        "telefone": "(19) 99708-7700",
        "cidade": "Piracicaba SP",
        "link": "http://www.emporiosantojoao.com.br"
    },
    {
        "nome": "Casa Vivá",
        "endereco": "Rua Dinarte Ribeiro, 128",
        "telefone": "(51) 3072-7028",
        "cidade": "Porto Alegre RS",
        "link": "https://casavivaqueijosevinhos.com.br"
    },
    {
        "nome": "Queijaria do Chico",
        "endereco": "Rua Jorge Tibiriçá, 3582",
        "telefone": "(17) 3235-1386 / (11) 97647-4263",
        "cidade": "São José do Rio Preto SP",
        "link": "https://queijaria-do-chico.negocio.site/"
    },
    {
        "nome": "Cave Queijos",
        "endereco": "R. das Dálias, 37",
        "telefone": "(71) 98884-7496 / (71) 98243-5411",
        "cidade": "Salvador BA",
        "link": "https://www.instagram.com/cavequeijos/"
    },
    {
        "nome": "Lá do Interior",
        "endereco": "Loja Online (atende Socorro e grande São Paulo)",
        "telefone": "(11) 96342-4457",
        "cidade": "Socorro SP",
        "link": "https://ladointerior.com.br/"
    },
    {
        "nome": "Cadim",
        "endereco": "Loja online (atende Vale do Paraíba e São Paulo)",
        "telefone": "(12) 99675-7387",
        "cidade": "Vale do Paraíba SP",
        "link": "https://www.instagram.com/queijoscadim/"
    },
    {
        "nome": "Tábua das Rosas",
        "endereco": "Rua das Rosas, 753 - Mirandópolis - São Paulo - SP",
        "telefone": "(11) 91874-3017",
        "cidade": "São Paulo SP",
        "link": "https://www.instagram.com/tabuadasrosas/"
    },
    {
        "nome": "Instituto Chão",
        "endereco": "R. Harmonia, 114, Vila Madalena, São Paulo SP",
        "telefone": "(11) 3819-4205",
        "cidade": "São Paulo SP",
        "link": "https://www.instagram.com/institutochao/"
    },
]

# Dicionário de estados e suas abreviações
estado_abreviacoes = {
    "SP": "São Paulo",
    "BA": "Bahia",
    "RS": "Rio Grande do Sul",
    "DF": "Distrito Federal",
    "Distrito Federal": "DF",
    "São Paulo": "SP",
    "Bahia": "BA",
    "Rio Grande do Sul": "RS"
}

# Função para exibir uma queijaria
def exibir_queijaria(queijaria):
    st.markdown(f"""
    <div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px; margin: 10px; flex: 1 1 30%; box-sizing: border-box;">
        <h3 style="margin-top: 0;"><a href="{queijaria['link']}" target="_blank" style="text-decoration: none; color: #007BFF;">{queijaria['nome']}</a></h3>
        <p><strong>Endereço:</strong> {queijaria['endereco']}<br><strong>Telefone:</strong> {queijaria['telefone']}</p>
    </div>
    """, unsafe_allow_html=True)

# Remover header e footer
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .css-1d391kg {padding-top: 2rem;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Adicionar campo de busca com autocomplete
termo_busca = st.text_input("Buscar queijaria ou cidade/estado")

# Exibir lista de queijarias por cidade
cidades = list(set(q["cidade"] for q in queijarias))
cidades.insert(0, "Todos")  # Adicionar opção "Todos" no início da lista
cidade_selecionada = st.selectbox("Selecione a cidade", cidades, index=0, key="selectbox", format_func=lambda x: x)

# Normalizar o termo de busca
termo_busca_normalizado = termo_busca.lower().strip()

# Função para verificar se a queijaria corresponde ao termo de busca
def corresponde_termo_busca(queijaria, termo):
    nome_corresponde = termo in queijaria["nome"].lower()
    cidade_corresponde = termo in queijaria["cidade"].lower()
    estado_corresponde = any(estado_abreviacoes.get(termo.upper(), "") in queijaria["cidade"].lower() for termo in estado_abreviacoes.keys())
    return nome_corresponde or cidade_corresponde or estado_corresponde

# Filtrar queijarias pela cidade selecionada e termo de busca
queijarias_filtradas = [
    q for q in queijarias 
    if (cidade_selecionada == "Todos" or q["cidade"] == cidade_selecionada) 
    and corresponde_termo_busca(q, termo_busca_normalizado)
]

# Container de cards
st.markdown("""
    <div style="display: flex; flex-wrap: wrap; justify-content: space-between;">
""", unsafe_allow_html=True)

# Exibir as queijarias filtradas
for queijaria in queijarias_filtradas:
    exibir_queijaria(queijaria)

# Fechar container de cards
st.markdown("</div>", unsafe_allow_html=True)

# Adiciona notificação de copyright
st.markdown("<div style='text-align: center; margin-top: 2rem;'>© 2024 <a href='https://queijista.com' target='_blank'>queijista</a> - Todos os direitos reservados.</div>", unsafe_allow_html=True)
