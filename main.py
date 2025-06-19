import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

# Configuración básica
bot = commands.Bot(command_prefix='$', intents=intents)

# Datos ecológicos
reciclaje_info = {
    "biologia": (
        "🌿 **BIOLOGÍA Y ECOLOGÍA** 🌿\n"
        "```diff\n"
        "+ La biología estudia:\n"
        "- Seres vivos y sus interacciones\n"
        "- Ecosistemas y biodiversidad\n"
        "- Impacto humano en la naturaleza\n"
        "```\n"
        "🔬 **APLICACIONES PRÁCTICAS:**\n"
        "```css\n"
        "[•] Conservación de especies\n"
        "[•] Biorremediación de suelos\n"
        "[•] Estudios climáticos\n"
        "```"
    ),
    "fenomenos": [
        "🌪️ **HURACANES** 🌪️\n"
        "```fix\n"
        "Causados por calentamiento oceánico\n"
        "```\n"
        "🛡️ **SOLUCIONES:**\n"
        "```diff\n"
        "+ Reducir emisiones\n"
        "+ Proteger manglares\n"
        "- Evitar deforestación costera\n"
        "```",

        "🔥 **INCENDIOS FORESTALES** 🔥\n"
        "```fix\n"
        "Prevención y control\n"
        "```\n"
        "🛡️ **MEDIDAS:**\n"
        "```diff\n"
        "+ Franjas cortafuegos\n"
        "+ Monitoreo satelital\n"
        "- No hacer fogatas en zonas prohibidas\n"
        "```",

        "🌊 **INUNDACIONES** 🌊\n"
        "```fix\n"
        "Control y mitigación\n"
        "```\n"
        "🛡️ **ACCIONES:**\n"
        "```diff\n"
        "+ Reforestación\n"
        "+ Sistemas de drenaje\n"
        "- Evitar construcción en llanuras de inundación\n"
        "```"
    ],
    "contaminacion": (
        "🚗 **CONTAMINACIÓN VEHICULAR** 🚗\n"
        "```yaml\n"
        "Problemas:\n"
        "  - Gases efecto invernadero\n"
        "  - Daño a la capa de ozono\n"
        "  - Partículas en suspensión\n"
        "```\n"
        "💡 **SOLUCIONES INTELIGENTES:**\n"
        "```diff\n"
        "+ Filtros para autos\n"
        "+ Transporte público eléctrico\n"
        "+ Uso de bicicletas\n"
        "- Reducir uso de vehículos privados\n"
        "```"
    ),
    "energias": (
        "⚡ **ENERGÍAS RENOVABLES** ⚡\n"
        "```asciidoc\n"
        "= Alternativas sostenibles =\n"
        "1. Solar :: Paneles fotovoltaicos\n"
        "2. Eólica :: Molinos de viento\n"
        "3. Hidroeléctrica :: Represas\n"
        "4. Geotérmica :: Calor terrestre\n"
        "5. Biomasa :: Materia orgánica\n"
        "```"
    )
}

# Consejos ecológicos prácticos
consejos_ecologicos = [
    "♻️ **Usa botellas de agua reutilizables** en lugar de comprar botellas de plástico",
    "🚲 **Considera caminar o usar bicicleta** para distancias cortas",
    "💡 **Apaga las luces** cuando salgas de una habitación",
    "🚰 **Cierra el grifo** mientras te cepillas los dientes",
    "🛒 **Lleva tus propias bolsas** al supermercado",
    "🌱 **Planta un árbol** o cuida plantas en tu hogar",
    "📱 **Desconecta cargadores** que no estés usando",
    "🍎 **Compra productos locales** y de temporada"
]

# Química sostenible
quimica_verde = [
    "🧪 **Usa productos de limpieza ecológicos** - menos tóxicos para el ambiente",
    "🚫 **Evita productos con ftalatos y parabenos** - dañinos para la salud",
    "♻️ **Recicla pilas y baterías** en contenedores especiales",
    "🌍 **Prefiere productos con envases biodegradables** - se descomponen naturalmente",
    "💧 **Ahorra agua** en tus experimentos químicos caseros"
]

# Manualidades con materiales reciclados
manualidades_reciclaje = [
    "🛋️ **Mueble con palets reciclados**:\n"
    "```md\n"
    "# Materiales:\n"
    "- Palets de madera\n"
    "- Lija\n"
    "- Pintura ecológica\n"
    "- Tornillos\n"
    "\n"
    "# Proceso:\n"
    "1. Limpiar y lijar los palets\n"
    "2. Pintar con pintura no tóxica\n"
    "3. Ensamblar según diseño (sofá, mesa, estante)\n"
    "```\n"
    "🌱 *Reduce la demanda de madera nueva*",

    "📦 **Organizadores con cajas de cartón**:\n"
    "```md\n"
    "# Materiales:\n"
    "- Cajas de cereales/zapatos\n"
    "- Tela o papel reciclado\n"
    "- Pegamento no tóxico\n"
    "\n"
    "# Proceso:\n"
    "1. Forrar las cajas con material decorativo\n"
    "2. Crear divisiones internas\n"
    "3. Apilar creativamente\n"
    "```\n"
    "🌱 *Reutiliza materiales que irían a la basura*",

    "🪴 **Macetas con botellas PET**:\n"
    "```md\n"
    "# Materiales:\n"
    "- Botellas plásticas\n"
    "- Tijeras\n"
    "- Pintura acrílica\n"
    "- Cuerda (opcional)\n"
    "\n"
    "# Proceso:\n"
    "1. Cortar la botella a la altura deseada\n"
    "2. Decorar con pintura\n"
    "3. Hacer agujeros de drenaje\n"
    "4. Colgar con cuerda (opcional)\n"
    "```\n"
    "🌱 *Da nueva vida al plástico*",

    "🎨 **Arte con tapas de botellas**:\n"
    "```md\n"
    "# Materiales:\n"
    "- Tapas plásticas/metalicas\n"
    "- Base de cartón/madera\n"
    "- Pegamento resistente\n"
    "\n"
    "# Proceso:\n"
    "1. Diseñar el patrón o imagen\n"
    "2. Pegar las tapas según diseño\n"
    "3. Crear mosaicos o figuras\n"
    "```\n"
    "🌱 *Transforma desechos en arte*",

    "🧵 **Billeteras con tetra packs**:\n"
    "```md\n"
    "# Materiales:\n"
    "- Envases de leche/jugo\n"
    "- Cierre de botón/hilo\n"
    "\n"
    "# Proceso:\n"
    "1. Lavar y abrir los envases\n"
    "2. Cortar según patrón\n"
    "3. Coser o pegar las partes\n"
    "```\n"
    "🌱 *Reutiliza materiales difíciles de reciclar*"
]

# Comandos básicos
@bot.command()
async def ayuda(ctx):
    """Muestra los comandos disponibles"""
    embed = discord.Embed(
        title="🌍 COMANDOS ECOBOT 🌎",
        description="```diff\n"
                    "+ Información científica verificada +\n"
                    "- Asesoría: Bióloga Karla Aparicio\n"
                    "- Química Prof. Lourdes Poveda\n"
                    "```",
        color=0x00ff00
    )
    
    embed.add_field(
        name="🔬 CIENCIA AMBIENTAL",
        value="```ini\n"
              "[$biologia] Fundamentos ecológicos\n"
              "[$fenomenos] Fenómenos naturales\n"
              "[$contaminacion] Soluciones ambientales\n"
              "[$energias] Energías renovables\n"
              "```",
        inline=False
    )
    
    embed.add_field(
        name="💡 ACCIONES PRÁCTICAS",
        value="```ini\n"
              "[$consejo] Consejo ecológico\n"
              "[$quimica] Química sostenible\n"
              "[$accion] Acción concreta para hoy\n"
              "[$manualidad] Idea de reciclaje creativo\n"
              "```",
        inline=False
    )
    
    embed.set_footer(text="¡Cada pequeña acción cuenta para nuestro planeta!")
    await ctx.send(embed=embed)

@bot.command()
async def biologia(ctx):
    """Explica la importancia de la biología en ecología"""
    await ctx.send(reciclaje_info["biologia"])

@bot.command()
async def fenomenos(ctx):
    """Información sobre fenómenos naturales"""
    await ctx.send(random.choice(reciclaje_info["fenomenos"]))

@bot.command()
async def contaminacion(ctx):
    """Soluciones para la contaminación"""
    await ctx.send(reciclaje_info["contaminacion"])

@bot.command()
async def energias(ctx):
    """Explica las energías renovables"""
    await ctx.send(reciclaje_info["energias"])

@bot.command()
async def consejo(ctx):
    """Envía un consejo ecológico práctico"""
    consejo = random.choice(consejos_ecologicos)
    await ctx.send(f"```diff\n+ CONSEJO ECOLÓGICO +\n```\n{consejo}")

@bot.command()
async def quimica(ctx):
    """Enseña sobre química sostenible"""
    consejo_quimico = random.choice(quimica_verde)
    await ctx.send(f"```fix\nQUÍMICA VERDE\n```\n{consejo_quimico}")

@bot.command()
async def accion(ctx):
    """Sugiere una acción concreta para ayudar"""
    acciones = [
        "🌿 **HOY PUEDES:** Separar tus residuos en orgánicos e inorgánicos",
        "♻️ **HOY PUEDES:** Reciclar una botella de plástico",
        "💡 **HOY PUEDES:** Cambiar una bombilla tradicional por una LED",
        "🚰 **HOY PUEDES:** Reducir tu tiempo de ducha en 2 minutos",
        "🛒 **HOY PUEDES:** Comprar un producto sin empaque plástico"
    ]
    await ctx.send(f"```css\n[ACCIÓN DEL DÍA]\n```\n{random.choice(acciones)}")

@bot.command()
async def manualidad(ctx):
    """Muestra una manualidad ecológica para hacer con reciclables"""
    await ctx.send(random.choice(manualidades_reciclaje))

# Eventos del bot
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Escribe $ayuda para salvar el planeta"))
    print(f'Bot listo como {bot.user.name}')

# Iniciar el bot
bot.run("TU TOKEN")  # Reemplaza con tu token real