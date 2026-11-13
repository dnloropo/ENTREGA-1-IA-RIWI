# Prompt utilizado para generar la pagina web

## Herramienta de IA utilizada
Claude (Anthropic)

## Contexto
Este proyecto se hizo como parte del reto "Prompt Engineering entre clanes" del bootcamp Riwi. Cada clan tenia que construir una aplicacion o pagina web usando ingenieria de prompts con una herramienta de IA.

## Resultado
Guerra de los Siete Reinos — un juego RPG web con:
- Mapa 3D explorable con 7 territorios de clanes (Three.js)
- Sistema de combate por turnos con habilidades, objetos y estados
- Personaje principal: Jesus David, el Forjador (Clan Ritchie)
- 7 enemigos campeon con habilidades unicas
- HUD con vida, energia, minimapa y sistema de misiones
- Controles por teclado (WASD/flechas) y d-pad tactil para movil
- Modo claro/oscuro automatico
- Dialogos narrativos antes y despues de cada batalla
- Sistema de niveles y progresion

## Prompt (resumen del proceso)
El juego se fue construyendo de forma iterativa con varios prompts conversacionales en Claude. El proceso fue mas o menos asi:

1. Primero se describio el concepto general: un RPG web basado en los 7 clanes del bootcamp Riwi (Ritchie, Turing, Tesla, Gosling, Van Rossum, Nakamoto, Ubuntu)
2. Se definio el heroe y la narrativa: el protagonista del clan Ritchie tiene que recorrer los territorios y enfrentar a los campeones de cada clan
3. Se fueron agregando cosas: mapa explorable con Three.js, sistema de combate por turnos, efectos visuales, balanceo de dificultad, sistema de misiones, cofre secreto con parkour
4. Se refino el diseno visual: tema medieval con tipografias Cinzel/Spectral, paleta de colores calida, animaciones de combate
5. Se optimizo para movil: d-pad tactil, responsive design, viewport-fit
