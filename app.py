import streamlit as st

st.set_page_config(
	page_title="Feliz cumple", page_icon=":rainbow:", initial_sidebar_state="collapsed"
)

tb1, tb2, tb3, tb4 =  st.tabs(["Y", "U", "L", "Y"])

with tb1:
	st.subheader("|Y|o estoy agradecido de haberte conocido")
	col1, col2 = st.columns(2, gap="small")
	with col1:
		st.image("Img/portada1.jpg")
		st.caption(
			"La imagen con la que te conoci, nunca se me olvida"
		)
	with col2:
		texto = f"""
		Querida YULY
		Hoy en tu día especial, deseo dedicarte unas palabras desde lo mas profundo de mi corazon.
		Aunque los años han pasado, mi afecto por ti permanece intacto. Eres una mujer excepcional
		que irradia luz por donde pasa con tu sonrisa contagiosa y tu bondadosa personalidad
		
		"El amor es asi, sufrido, esbenigno... no busca lo suyo..." (1 Corintios 13:4-5).
		Así ha sido mi cariño por ti, desinteresado y puro como el de la amistad mas sincera. 
		Ojalá que la vida te siga colmando de dicha y prosperidad. Te mereces lo mejor.
		
		Que tu camino esté siempre iluminado y que dios derrame incontables bendiciones sobre ti.
		Feliz cumpleaños, amiga mia, amor mio. Con aprecio profundo YO
		
		Si pudiera darte una cosa en la vida, te daría la capacidad de verte a ti misma
		a través de mis ojos, solo así te darías cuenta de lo especial que eres para mí
		"""
		st.write(texto)
with tb2:
	st.subheader("|U|na sola vez te vi... fue suficiente para mi")
	tb_col1, tb2_col2 = st.columns(2, gap="small")
	with tb_col1:
		st.image("Img/portada2.jpg")
		st.caption("Siempre he estado orgulloso de ti, de todo")
	with tb2_col2:
		texto2 = f"""
		Para una mujer tan única como tú:                  
		Que tu espíritu y energía guien tus pasos siempre adelante en esta vida...
		que la luz de la alegría ilumine cada nuevo día, pues una sonrisa tuya podría cambiar el mundo.
		
		"La belleza de una mujer no está en el vestido que usa, la figura que muestra o la forma
		en que se peina el cabello. La belleza de una mujer debe ser vista desde en sus ojos, 
		porque esa es la puerta a su corazón, el lugar donde el amor reside". (Audrey hepburn)
		Tus ojos reflejan la bondad de tu alma 
		"""
		st.write(texto2)
