import streamlit as st
from PIL import Image
import os



 # Configurando a largura da tela e ativando o desativando o sidebar
st.set_page_config(
    page_title="Painel de Qualidade",
    layout='wide',
    page_icon=":bar_chart:",
    initial_sidebar_state="expanded",
                   )


# Formulários

qrcode_carregamento_1_nivel = r'qrcode_survey/carregamento_1_nivel.png'

qrcode_carregamento_logistica = r'qrcode_survey/carregamento_logistica.png'

qrcode_desperdicio = r'qrcode_survey/desperdicio.png'

qrdcode_estradas_v1 = r'qrcode_survey/estradas_v1.png'

qrcode_estradas = r'qrcode_survey/estradas.png'

qrcode_apont_prod = r'qrcode_survey/prod_segundo_nivel.png'

qrcode_prod_tecnicos = r'qrcode_survey/prod_tecnicos.png'

qrcode_plantio = r'qrcode_survey/plantio.png'

qrcode_preparo = r'qrcode_survey/preparo_solo.png'

qrcode_adub_herb_prec = r'qrcode_survey/adub_herb_prec.png'

qrcode_aducob = r'qrcode_survey/adub_cob.png'

qrcode_irrig = r'qrcode_survey/irrigacao.png'

qrcode_form_dose = r'qrcode_survey/formiga_dose.png'

qrcode_form_acmp = r'qrcode_survey/formiga_acom.png'

qrcode_pulverizacao = r'qrcode_survey/pulverizacao.png'

qrcode_harvest = r'qrcode_survey/harvester.PNG'

qrcode_forwarder = r'qrcode_survey/forwarder.PNG'

qrcode_1selecao = r'qrcode_survey/1_selecao.png'

qrcode_2selecao = r'qrcode_survey/2_selecao.png'

qrcode_plantio_estacas = r'qrcode_survey/plantio_de_estacas.png'

qrcode_minijardim = r'qrcode_survey/mini_jardim.png'

qrcode_qualidesk = r'qrcode_survey/qualidesk.png'



# Foto Time São Paulo


gabriel = r'Colaboradores/gabriel.png'

adriana = r"Colaboradores/Adriana.jpg"

daniel = r'Colaboradores/Daniel.jpg'

rafael = r'Colaboradores/Rafael.jpg'

thiago = r'Colaboradores/Thiago.png'

leticia = r'Colaboradores/leticia.jpg'

renan = r'Colaboradores/renan.jpg'

maria = r'Colaboradores/maria.jpg'

thasso = r'Colaboradores/thasso.png'



# Icones

icone_silv =r'icones/silvicultura.png'

icone_viv = r'icones/viveiros.png'

icone_log = r'icones/carregamento.png'

icone_col = r'icones/colheita.png'

icone_plan = r'icones/planejamento.png'

icone_sop = r'icones/sop.png'

icone_treinamentos = r'icones/treinamento.png'



#Power Bi

pbi_carregamento = r'https://app.powerbi.com/groups/8f026f89-78ef-45ac-957e-15ae919e99fc/reports/a521c293-a0ae-4ff4-8326-de0ff3d98f44/ReportSection?experience=power-bi'

pbi_silvicultura = r'https://app.powerbi.com/groups/8f026f89-78ef-45ac-957e-15ae919e99fc/reports/2b3bbb87-aae4-40b1-8c33-89c298cc16e9/ReportSectionb66afd3c296f365a01f1?experience=power-bi'

pbi_aderencia = r'https://app.powerbi.com/groups/8f026f89-78ef-45ac-957e-15ae919e99fc/reports/0db073cb-4d4d-49a7-b7fb-a848c0400532/ReportSection?experience=power-bi'

pbi_sobrevivencia = r'https://app.powerbi.com/groups/8f026f89-78ef-45ac-957e-15ae919e99fc/reports/e182956b-8ff1-4b4e-81bb-3b0b487f0c74/ReportSection?experience=power-bi&ctid=582d9d84-4800-4487-9b24-cdc6471551ae'

pbi_cadastro = r'https://app.powerbi.com/reportEmbed?reportId=564a7c83-00f4-460d-ad84-315478f4a48c&autoAuth=true&ctid=582d9d84-4800-4487-9b24-cdc6471551ae'

pbi_colheita = r'https://app.powerbi.com/groups/8f026f89-78ef-45ac-957e-15ae919e99fc/reports/4d02f0c0-4cfb-4f1c-8290-f610f5c7e6e7/ReportSection?experience=power-bi&ctid=582d9d84-4800-4487-9b24-cdc6471551ae'

pbi_desenvolvimento = r'https://app.powerbi.com/reportEmbed?reportId=c46a6580-ba63-4a13-806e-de7d1ffc174c&autoAuth=true&ctid=582d9d84-4800-4487-9b24-cdc6471551ae'

pbi_qld_torre = r'https://app.powerbi.com/groups/8f026f89-78ef-45ac-957e-15ae919e99fc/reports/90c9ffd9-4220-4a6f-a384-a551e869ead9/ReportSection?experience=power-bi'

pbi_treinamentos = r'https://app.powerbi.com/groups/8f026f89-78ef-45ac-957e-15ae919e99fc/reports/9c03ebba-c989-45e8-b5ca-032309303ca4/ReportSectionba60a7c5ba98c77b20e0?experience=power-bi'

pbi_viveiros = r'https://app.powerbi.com/groups/8f026f89-78ef-45ac-957e-15ae919e99fc/reports/1572afba-d051-4888-b6b8-97fe04dd06ae/ReportSection?experience=power-bi'

pbi_carregamento_entrega = r'https://app.powerbi.com/groups/8f026f89-78ef-45ac-957e-15ae919e99fc/reports/10b4b397-0ef4-4a15-b8b1-45b30f5d8579/ReportSection2dd9f9e5023419e6ce5a?experience=power-bi'

pbi_plan_colheita = r'https://app.powerbi.com/groups/8f026f89-78ef-45ac-957e-15ae919e99fc/reports/4a2daa8d-8081-4bf2-9baa-92c307f3e5e5/ReportSection?experience=power-bi'

pbi_plan_estradas = r'https://app.powerbi.com/groups/8f026f89-78ef-45ac-957e-15ae919e99fc/reports/b9d034e7-bd77-4239-bb2a-5f79174c2557/ReportSection?experience=power-bi'

pbi_sop = r'https://app.powerbi.com/Redirect?action=OpenApp&appId=6e3e4053-398d-4f70-9c59-480559b0288b&ctid=582d9d84-4800-4487-9b24-cdc6471551ae&experience=power-bi'

pbi_treinamento = r'https://app.powerbi.com/groups/me/reports/bf42d3fa-4530-4eaf-ae33-f8f7e05199a1/ReportSection?ctid=582d9d84-4800-4487-9b24-cdc6471551ae&experience=power-bi'


#paths

#Planejamento
path_mapas = r'\\GLWFS02\UTILITARIOS\Publica\Florestal\Relatórios de Qualidade\Mapas de Parcelas'

path_prod_seg_nivel = r'\\GLWFS02\LWC-FLORESTAL\Qualidade_Florestal\01- SÃO PAULO\10- Planejamento e Controle 2°nível\2023\01 - Silvicultura\03- Relatórios\Produção_Segundo_Nível _ consulta.xlsx'

path_prog_sobrevivencia = r"\\GLWFS02\LWC-FLORESTAL\Qualidade_Florestal\01- SÃO PAULO\10- Planejamento e Controle 2°nível\2023\12 - Programações Sobrevivência\05 - Equilíbrio\Programação_Sobrevivência - SP.xlsx"



#Logistica
path_carreg_1_nivel = r'\\GLWFS02\LWC-FLORESTAL\Qualidade_Florestal\01- SÃO PAULO\04- Logística, transporte e estradas\00 - Bases de Trabalho\Carregamento Primeiro Nível\AvaliacaodeQualidadeCarregamento1XNivel_attachments'

path_estradasv1 = r'\\GLWFS02\LWC-FLORESTAL\Qualidade_Florestal\01- SÃO PAULO\04- Logística, transporte e estradas\00 - Bases de Trabalho\Carregamento Primeiro Nível\LogisticaFlorestalEstradasV1_attachments'

path_estradas = r'\\GLWFS02\LWC-FLORESTAL\Qualidade_Florestal\01- SÃO PAULO\04- Logística, transporte e estradas\00 - Bases de Trabalho\Carregamento Primeiro Nível\QualidadeEstradasFlorestais_attachments'

path_carregamento_logistica = r'\\GLWFS02\LWC-FLORESTAL\Qualidade_Florestal\01- SÃO PAULO\04- Logística, transporte e estradas\00 - Bases de Trabalho\QualidadeFlorestalCarregamentoLogistica_attachments'



#Silvicultura
path_silv = r'\\Glwfs02\utilitarios\Publica\Florestal\Relatórios de Qualidade\Avaliações de 2º nível de Silvicultura\Relatórios operacionais\SP\2023'




#icones

mudas = r'icones/plant.png'

calendario = r'icones/calendario.png'

cadastro = r'icones/cadastro.png'

loading = r'icones/loading.png'

logo_path = r'icones/logo - Bracell.jpg'

torre_path = r'icones/torre.png'

plan_col = r'icones/planejamento_col.png'

plan_estradas = r'icones/estradas.png'

#contatos

leticia_e = 'lcury'

thiago_e = 'ttelatin'

daniel_e = 'dlcarvalho'

renan_e = 'razambuja'

adriana_e = 'asroliveira'

gabriel_e = 'gamoura'




def home_page():

    st.image(Image.open(logo_path).resize((200, 50)))

    st.subheader("Painel de Qualidade")

    st.write('<b>São Paulo</b>', unsafe_allow_html=True)

    st.markdown('<hr style="border-top: 1px solid #40d925;">',unsafe_allow_html=True)


    #Container de Títulos
    with st.container():
        st.subheader('Indicadores')


    #Container de Fotos
    with st.container():

        col1, col2, col3, col4, col5 , col6, col7 = st.columns(7)

        col1.image(Image.open(icone_viv).resize((100, 100)))

        col2.image(Image.open(icone_silv).resize((110,110)))

        col3.image(Image.open(icone_log).resize((100,100)))

        col4.image(Image.open(icone_col).resize((100,100)))

        col5.image(Image.open(icone_plan).resize((100,100)))

        col6.image(Image.open(icone_sop).resize((115,115)))

        col7.image(Image.open(icone_treinamentos).resize((95,95)))


    #Container de indicadores

    with st.container():

        col11, col12,col13,col14,col15,col16, col17 = st.columns(7)

        col11.markdown(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Viveiro]({pbi_viveiros})',unsafe_allow_html = True)

        col12.markdown(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Silvicultura]({pbi_silvicultura})',unsafe_allow_html = True)

        col13.markdown(f'[Logística Florestal]({pbi_carregamento})',unsafe_allow_html = True)

        col14.markdown(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Colheita]({pbi_colheita})',unsafe_allow_html = True)

        col15.markdown(f'&nbsp;[Planejamento]({pbi_aderencia})',unsafe_allow_html = True)

        col16.markdown(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SOP]({pbi_sop})',unsafe_allow_html=True)

        col17.markdown(f'&nbsp;[Treinamentos]({pbi_treinamento})',unsafe_allow_html = True)


    #Container de e-mails
    #with st.container():
    #    st.write('')

    #    st.write('<b>E-mails:</b>',unsafe_allow_html = True)

    #   col21,col22,col23,col24,col25 = st.columns(5)

    #    col21.write(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'+leticia_e)

    #   col22.write(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'+thiago_e)

    #    col23.write(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'+daniel_e)
        
    #    col24.write(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'+renan_e)

    #   col25.write(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'+adriana_e)


def viveiro():
    
    st.image(Image.open(maria).resize((100,100)))


    st.image(Image.open(logo_path).resize((200, 50)))

    st.subheader("Viveiro")

    st.write('<b>Controles de Viveiros</b>', unsafe_allow_html=True)

    st.markdown('<hr style="border-top: 1px solid #40d925;">',unsafe_allow_html=True)


#container de desenvolvimento
    with st.container():
        
        st.subheader("Coletores de Qualidade")
        st.write('')
        st.write('')
        st.write('')

        _,viv_col1,_,viv_col2,_,viv_col3,_, viv_col4,_ = st.columns(9)

        viv_col1.image(Image.open(qrcode_1selecao).resize((200,200)))

        viv_col1.write("&nbsp;&nbsp;Survey - 1ª Seleção")

        viv_col2.image(Image.open(qrcode_2selecao).resize((200,200)))

        viv_col2.write("&nbsp;&nbsp;Survey - 2ª Seleção")

        viv_col3.image(Image.open(qrcode_plantio_estacas).resize((200,200)))

        viv_col3.write("&nbsp;&nbsp;Survey - Plantio Estacas")

        viv_col4.image(Image.open(qrcode_minijardim).resize((200,200)))

        viv_col4.write("&nbsp;&nbsp;Survey - Mini Jardim")



def silvicultura():
   
    st.image(Image.open(thiago).resize((110,110)))


    st.image(Image.open(logo_path).resize((200, 50)))

    st.subheader("Silvicultura")

    st.write('<b>Controles de Silvicultura</b>', unsafe_allow_html=True)

    st.markdown('<hr style="border-top: 1px solid #40d925;">',unsafe_allow_html=True)

    #Informações dos qrcodes
    with st.container():

        #retirado parte de treinamentos

        #st.subheader("Indicadores")
        
        #_,_,tsilv1,_,_ = st.columns(5)

        #tsilv1.image(Image.open(torre_path).resize((75,75)))

        #tsilv1.markdown(f'[Treinamentos]({pbi_treinamentos})')


        st.subheader("Coletores de Qualidade")
        st.write('')
        st.write('')
        st.write('')


        silv1,_,silv2,_,silv3,_,silv4,_ = st.columns(8)


        silv1.image(Image.open(qrcode_form_dose).resize((200,200)))

        silv1.write("&nbsp;&nbsp;Survey - Formiga Dose")

        silv2.image(Image.open(qrcode_form_acmp).resize((200,200)))

        silv2.write(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Survey - Formiga',unsafe_allow_html=True)
        silv2.write(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Acompanhamento',unsafe_allow_html=True)



        silv3.image(Image.open(qrcode_preparo).resize((200,200)))

        silv3.write(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Survey - Preparo',unsafe_allow_html=True)


        silv4.image(Image.open(qrcode_plantio).resize((200,200)))
        silv4.write(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Survey - Plantio',unsafe_allow_html=True)


        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')



        silv5,_,silv6,_,silv7,_,silv8,_ = st.columns(8)

        silv5.image(Image.open(qrcode_irrig))
        silv5.write(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Survey - Irrigação',unsafe_allow_html=True)


        silv6.image(Image.open(qrcode_aducob).resize((200,200)))
        silv6.write(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Survey - Adubação',unsafe_allow_html=True)
        silv6.write(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;De Cobertura',unsafe_allow_html=True)


        silv7.image(Image.open(qrcode_adub_herb_prec).resize((200,200)))
        silv7.write(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Survey - Adubação',unsafe_allow_html=True)
        silv7.write(f'&nbsp;E herbicida de Precisão',unsafe_allow_html=True)



        silv8.image(Image.open(qrcode_pulverizacao).resize((200,200)))
        silv8.write(f'&nbsp;&nbsp;&nbsp;&nbsp;Survey - Pulverização',unsafe_allow_html=True)


def carregamento():
    st.image(Image.open(daniel).resize((100,100)))

    st.image(Image.open(logo_path).resize((200, 50)))

    st.subheader("Logística Florestal")

    st.write('<b>Controles de Logística Florestal: Manutenção de Estradas, Carregamento e Transporte Florestal</b>', unsafe_allow_html=True)

    st.markdown('<hr style="border-top: 1px solid #40d925;">',unsafe_allow_html=True)


#container de paths
    #with st.container():

        #st.subheader('Consultas')
        #st.write('')
        #st.write('')
        #st.write('')

        #log_path1, log_path2, log_path3,log_path4,_ = st.columns(5)

        #if log_path1.button("Evidência de Estradas", type ='secondary'):
            #os.startfile(path_estradas)

        #if log_path2.button("Evidência de Estradas NP", type ='secondary'):
            #os.startfile(path_estradasv1)

        #if log_path3.button("Carregamento 1° Nível", type ='secondary'):
            #os.startfile(path_carreg_1_nivel)

        #if log_path4.button("Carregamento 2° Nível", type ='secondary'):
            #os.startfile(path_carregamento_logistica)

        #st.write('')
        #st.write('')
        #st.write('')
        #st.write('')
    with st.container():

        st.subheader("Indicadores")
        lcarr,_,_ ,_,_,_,_ = st.columns(7)

        lcarr.image(Image.open(cadastro).resize((150,150)))

        st.markdown(f'&nbsp;&nbsp;&nbsp;&nbsp;[Classificação de Talhões]({pbi_carregamento_entrega})')



#container de qrcodes

    with st.container():
        st.subheader("Coletores de Qualidade")
        st.write('')
        st.write('')
        st.write('')

        log1,log2,log3,log4,log5 = st.columns(5)

        log1.image(Image.open(qrcode_estradas).resize((200,200)))

        log2.image(Image.open(qrdcode_estradas_v1).resize((200,200)))

        log3.image(Image.open(qrcode_carregamento_1_nivel).resize((200,200)))
        
        log4.image(Image.open(qrcode_carregamento_logistica).resize((200,200)))

        log5.image(Image.open(qrcode_desperdicio).resize((200,200)))

        

#container de legendas
    with st.container():

        log11,log12,log13,log14,log15 = st.columns(5)

        log11.write(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Survey Estradas',unsafe_allow_html = True)

        log12.write(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Survey Estradas',unsafe_allow_html = True)
        log12.write(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Novo Procedimento',unsafe_allow_html = True)

        log13.write(f'Survey - Carregamento 1° Nível')
        
        log14.write(f'Survey - Carregamento 2° Nível')

        log15.write(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Survey - Desperdício', unsage_allow_html = True)


def colheita():
    
    st.image(Image.open(daniel).resize((100,100)))


    st.image(Image.open(logo_path).resize((200, 50)))

    st.subheader("Colheita")

    st.write('<b>Controles de Colheita</b>', unsafe_allow_html=True)

    st.markdown('<hr style="border-top: 1px solid #40d925;">',unsafe_allow_html=True)



#container de desenvolvimento
    with st.container():

        st.subheader('Coletores de Qualidade')

        _,_,col1,_,_,col2,_,_ = st.columns(8)


        col1.image(Image.open(qrcode_harvest).resize((200,200)))

        col2.image(Image.open(qrcode_forwarder).resize((200,200)))

        col1.write(f'&nbsp;&nbsp;&nbsp;Survey - Harvester')

        col2.write(f'&nbsp;&nbsp;&nbsp;Survey - Forwarder')



def planejamento():
    
    st.image(Image.open(adriana).resize((100,100)))

    st.image(Image.open(logo_path).resize((200, 50)))

    st.subheader("Planejamento")

    st.write('<b>Controles de Planejamento</b>', unsafe_allow_html=True)

    st.markdown('<hr style="border-top: 1px solid #40d925;">',unsafe_allow_html=True)


#container de paths

    #with st.container():

        #st.subheader('Consultas')
        #st.write('')
        #st.write('')
        #st.write('')

        #planpath1,planpath2,planpath3 = st.columns(3)

        #if planpath1.button("Mapas de Parcelas", type ='secondary'):
            #os.startfile(path_mapas)
       
     
        #if planpath2.button('Programação de Sobrevivência'):
            #os.startfile(path_prog_sobrevivencia)

        #if planpath3.button('Consulta de Produção Segundo Nível'):
            #os.startfile(path_prod_seg_nivel)
        
        #st.write('')
        #st.write('')
        #st.write('')
        #st.write('')


#container dos ícones
    with st.container():

        st.subheader("Indicadores")
        _,lplan1,_ ,lplan2,_ ,lplan3,_ ,lplan4,_,lplan5,_= st.columns(11)


        lplan1.image(Image.open(calendario).resize((100,100)))

        lplan2.image(Image.open(mudas).resize((100,100)))
        
        lplan3.image(Image.open(plan_col).resize((100,100)))
        
        lplan4.image(Image.open(plan_estradas).resize((100,100)))

        lplan5.image(Image.open(cadastro).resize((100,100)))


#container dos links power bi
    with st.container():

        _,lplan11,_,lplan12,_,lplan13,_,lplan14,_,lplan15,_ = st.columns(11)

        lplan11.markdown(f'&nbsp;&nbsp;&nbsp;&nbsp;[Silvicultura]({pbi_aderencia})')

        lplan12.markdown(f'[Sobrevivência]({pbi_sobrevivencia})')
         
        lplan13.markdown(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Colheita]({pbi_plan_colheita})')

        lplan14.markdown(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Estradas]({pbi_plan_estradas})')

        lplan15.markdown(f'&nbsp;&nbsp;&nbsp;&nbsp;[Cadastro]({pbi_cadastro})')


#container do qrcode
    with st.container():
        st.write('')
        st.write('')
        st.write('')
        st.write('')



        st.subheader('Coletores de Qualidade')

        st.write('')
        st.write('')
        st.write('')

        _,plan1,_,plan2,_ = st.columns(5)

        plan1.image(Image.open(qrcode_estradas).resize((200,200)))

        plan2.image(Image.open(qrcode_prod_tecnicos).resize((200,200)))
        

#container da legenda qrcode
    with st.container():

        _,plan31,_,plan32,_ = st.columns(5)

        plan31.write(f'&nbsp;&nbsp;&nbsp;Survey - Produção 2° Nível')

        plan32.write(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Survey - Técnicos')
        

def torre():
    st.image(Image.open(thasso).resize((100,100)))
    
    st.image(Image.open(logo_path).resize((200, 50)))

    st.subheader("Qualidade 4.0")

    st.write('<b>Controles da Transformação digital</b>', unsafe_allow_html=True)

    st.markdown('<hr style="border-top: 1px solid #40d925;">',unsafe_allow_html=True)

#container de desenvolvimento
    with st.container():
        st.subheader("Indicadores")
        qld_col1,_,_,_,_ = st.columns(5)

        qld_col1.image(Image.open(torre_path).resize((100,100)))
                
        qld_col1.markdown(f'&nbsp;&nbsp;&nbsp;&nbsp;[Indicadores]({pbi_qld_torre})')


    #container de desenvolvimento
    with st.container():

        st.subheader('Coletor Qualidesk')

        _,_,col1,_,_= st.columns(5)
        _,_,text1,_,_ = st.columns(5)


        col1.image(Image.open(qrcode_qualidesk).resize((200,200)))
        
        text1.write(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Survey - Qualidesk')


#Botões e Páginas
with st.container():
    st.sidebar.title('Navegação')
    paginas = ['Home Page','Viveiro', 'Silvicultura', 'Logística Florestal', 'Colheita', 'Planejamento', 'Qualidade 4.0']
    escolha_pagina = st.sidebar.radio('Escolha uma página', paginas, index=0)

    if escolha_pagina == 'Home Page':
        home_page()
    elif escolha_pagina == 'Viveiro':
        viveiro()
    elif escolha_pagina == 'Silvicultura':
        silvicultura()
    elif escolha_pagina == 'Logística Florestal':
        carregamento()
    elif escolha_pagina == 'Colheita':
        colheita()
    elif escolha_pagina == 'Planejamento':
        planejamento()

    elif escolha_pagina == 'Qualidade 4.0':
        torre()

