import streamlit as st
import gspread
from google.oauth2.service_account import Credentials


# =========================================================
# CONFIGURACIÓN
# =========================================================

st.set_page_config(
    page_title="TecMinators Pit Scouting",
    page_icon="",
    layout="centered"
)


# =========================================================
# GOOGLE SHEETS
# =========================================================

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]


@st.cache_resource
def conectar_google_sheets():
    credentials = Credentials.from_service_account_info(
        dict(st.secrets["gcp_service_account"]),
        scopes=SCOPES
    )

    client = gspread.authorize(credentials)

    spreadsheet = client.open_by_key(
        "1sGoESN2GVpw_n_Y32VvcA5ROYNCy_SCTuFZ8--ifwVw"
    )

    worksheet = spreadsheet.worksheet("Pit Scouting")

    return worksheet


# =========================================================
# ESTILO
# =========================================================

st.markdown("""
<style>

.block-container {
    max-width: 700px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.section {
    background-color: #151515;
    padding: 18px;
    border-radius: 12px;
    margin-top: 20px;
    margin-bottom: 20px;
}

.section-title {
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 15px;
}

.score-card {
    background-color: #151515;
    padding: 20px;
    border-radius: 12px;
    margin-top: 20px;
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# TÍTULO
# =========================================================

st.title("TecMinators Pit Scouting")
st.caption("FTC BIOBUZZ 2026–2027")


# =========================================================
# INFORMACIÓN DEL EQUIPO
# =========================================================

st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">1. Información del equipo</div>',
    unsafe_allow_html=True
)

team_number = st.number_input(
    "Número de equipo",
    min_value=1,
    step=1
)

team_name = st.text_input(
    "Nombre del equipo"
)

robot_name = st.text_input(
    "Nombre del robot"
)

st.markdown('</div>', unsafe_allow_html=True)


# =========================================================
# DRIVETRAIN
# =========================================================

st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">2. Drivetrain</div>',
    unsafe_allow_html=True
)

drivetrain = st.selectbox(
    "Tipo de drivetrain",
    [
        "Mecanum",
        "Tank",
        "X-Drive",
        "Otro"
    ]
)

drive_motors = st.number_input(
    "Número de motores",
    min_value=0,
    max_value=8,
    value=4,
    step=1
)

drive_speed = st.slider(
    "Velocidad",
    min_value=1,
    max_value=5,
    value=3
)

st.markdown('</div>', unsafe_allow_html=True)


# =========================================================
# AUTO
# =========================================================

st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">3. AUTO</div>',
    unsafe_allow_html=True
)

has_auto = st.checkbox(
    "Tiene autónomo"
)

auto_scoring = st.checkbox(
    "Realiza scoring durante AUTO"
)

auto_park = st.checkbox(
    "Puede hacer Park durante AUTO"
)

auto_consistency = st.slider(
    "Consistencia del autónomo",
    min_value=1,
    max_value=5,
    value=3
)

auto_actions = st.multiselect(
    "¿Qué realiza durante AUTO?",
    [
        "Sale de la zona",
        "Hive Tips",
        "Pollen en Cell",
        "Nectar en Cell",
        "Pollen en Flowers",
        "Nectar en Flowers",
        "Bottom Nectar Bonus",
        "Pollen en Garden",
        "Nectar en Garden",
        "Park"
    ]
)

st.markdown('</div>', unsafe_allow_html=True)


# =========================================================
# TELEOP / SCORING
# =========================================================

st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">4. TELEOP / SCORING</div>',
    unsafe_allow_html=True
)

teleop_hive_tips = st.checkbox(
    "Puede hacer Hive Tips"
)

teleop_cell_pollen = st.checkbox(
    "Puede colocar Pollen en Cell"
)

teleop_cell_nectar = st.checkbox(
    "Puede colocar Nectar en Cell"
)

teleop_flower_pollen = st.checkbox(
    "Puede colocar Pollen en Flowers"
)

teleop_flower_nectar = st.checkbox(
    "Puede colocar Nectar en Flowers"
)

bottom_nectar_bonus = st.checkbox(
    "Puede hacer Bottom Nectar Bonus"
)

garden_pollen = st.checkbox(
    "Puede colocar Pollen en Garden"
)

garden_nectar = st.checkbox(
    "Puede colocar Nectar en Garden"
)

scoring_speed = st.slider(
    "Velocidad de scoring",
    min_value=1,
    max_value=5,
    value=3
)

st.markdown('</div>', unsafe_allow_html=True)


# =========================================================
# MECANISMOS
# =========================================================

st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">5. Mecanismos</div>',
    unsafe_allow_html=True
)

intake = st.checkbox(
    "Intake"
)

shooter_scorer = st.checkbox(
    "Shooter / Scorer"
)

feeder = st.checkbox(
    "Feeder"
)

turret = st.checkbox(
    "Turret"
)

lift = st.checkbox(
    "Lift"
)

mechanism_sensors = st.multiselect(
    "Sensores",
    [
        "Encoder",
        "Pinpoint",
        "IMU",
        "Color Sensor",
        "Distance Sensor",
        "Vision",
        "AprilTag",
        "Otro"
    ]
)

other_mechanisms = st.multiselect(
    "Otros mecanismos",
    [
        "Extensión",
        "Articulación",
        "Servo",
        "Wrist",
        "Claw",
        "Otro"
    ]
)

st.markdown('</div>', unsafe_allow_html=True)


# =========================================================
# END GAME
# =========================================================

st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">6. END GAME</div>',
    unsafe_allow_html=True
)

endgame_park = st.checkbox(
    "Puede hacer Park durante END GAME"
)

endgame_other = st.multiselect(
    "Otros mecanismos de END GAME",
    [
        "Hang",
        "Ascend",
        "Lift",
        "Extensión",
        "Otro"
    ]
)

endgame_time = st.selectbox(
    "Tiempo aproximado para END GAME",
    [
        "No realiza",
        "Más de 15 s",
        "10–15 s",
        "5–10 s",
        "Menos de 5 s"
    ]
)

endgame_consistency = st.slider(
    "Consistencia del END GAME",
    min_value=1,
    max_value=5,
    value=3
)

st.markdown('</div>', unsafe_allow_html=True)


# =========================================================
# DEFENSA
# =========================================================

st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">7. DEFENSA</div>',
    unsafe_allow_html=True
)

can_defend = st.checkbox(
    "Puede jugar defensa"
)

can_resist_defense = st.checkbox(
    "Puede resistir defensa"
)

maneuverability = st.slider(
    "Maniobrabilidad",
    min_value=1,
    max_value=5,
    value=3
)

st.markdown('</div>', unsafe_allow_html=True)


# =========================================================
# PROGRAMACIÓN
# =========================================================

st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">8. PROGRAMACIÓN</div>',
    unsafe_allow_html=True
)

programming_language = st.multiselect(
    "Lenguaje",
    [
        "Java",
        "Blocks",
        "OnBot Java",
        "Otro"
    ]
)

pathing = st.checkbox(
    "Pedro Pathing"
)

pinpoint = st.checkbox(
    "Pinpoint"
)

vision = st.checkbox(
    "Vision"
)

apriltags = st.checkbox(
    "AprilTags"
)

pid = st.checkbox(
    "PID"
)

other_software = st.multiselect(
    "Otros sensores / software",
    [
        "Road Runner",
        "FTCLib",
        "Limelight",
        "OpenCV",
        "Odometry",
        "IMU",
        "Otro"
    ]
)

st.markdown('</div>', unsafe_allow_html=True)


# =========================================================
# CONFIABILIDAD
# =========================================================

st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">9. CONFIABILIDAD</div>',
    unsafe_allow_html=True
)

drivetrain_reliability = st.slider(
    "Drivetrain",
    min_value=1,
    max_value=5,
    value=3
)

intake_reliability = st.slider(
    "Intake",
    min_value=1,
    max_value=5,
    value=3
)

scoring_reliability = st.slider(
    "Scoring",
    min_value=1,
    max_value=5,
    value=3
)

auto_reliability = st.slider(
    "Autónomo",
    min_value=1,
    max_value=5,
    value=3
)

endgame_reliability = st.slider(
    "End Game",
    min_value=1,
    max_value=5,
    value=3
)

known_problems = st.multiselect(
    "Problemas conocidos",
    [
        "Drivetrain",
        "Intake",
        "Scoring",
        "Autónomo",
        "End Game",
        "Sensores",
        "Software",
        "Ninguno"
    ]
)

st.markdown('</div>', unsafe_allow_html=True)


# =========================================================
# ESTRATEGIA / NOTAS
# =========================================================

st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">10. ESTRATEGIA / NOTAS</div>',
    unsafe_allow_html=True
)

strengths = st.multiselect(
    "Fortalezas",
    [
        "Velocidad",
        "Scoring",
        "Autónomo",
        "End Game",
        "Defensa",
        "Maniobrabilidad",
        "Confiabilidad",
        "Consistencia"
    ]
)

weaknesses = st.multiselect(
    "Debilidades",
    [
        "Velocidad",
        "Scoring",
        "Autónomo",
        "End Game",
        "Defensa",
        "Maniobrabilidad",
        "Confiabilidad",
        "Consistencia"
    ]
)

observed_strategy = st.multiselect(
    "Estrategia observada",
    [
        "Scoring rápido",
        "Scoring consistente",
        "Prioriza defensa",
        "Evita defensa",
        "Prioriza Flowers",
        "Prioriza Cell",
        "Prioriza Garden",
        "Prioriza End Game"
    ]
)

comments = st.text_area(
    "Comentarios",
    placeholder="Escribe aquí cualquier observación adicional..."
)

st.markdown('</div>', unsafe_allow_html=True)


# =========================================================
# GUARDAR
# =========================================================

st.markdown("---")

if st.button(
    "GUARDAR PIT SCOUTING",
    type="primary",
    use_container_width=True
):

    if team_number == 0:
        st.error("Ingresa un número de equipo.")
        st.stop()

    scouting_data = [
        team_number,
        team_name,
        robot_name,
        drivetrain,
        drive_motors,
        drive_speed,
        has_auto,
        auto_scoring,
        auto_park,
        auto_consistency,
        ", ".join(auto_actions),
        teleop_hive_tips,
        teleop_cell_pollen,
        teleop_cell_nectar,
        teleop_flower_pollen,
        teleop_flower_nectar,
        bottom_nectar_bonus,
        garden_pollen,
        garden_nectar,
        scoring_speed,
        intake,
        shooter_scorer,
        feeder,
        turret,
        lift,
        ", ".join(mechanism_sensors),
        ", ".join(other_mechanisms),
        endgame_park,
        ", ".join(endgame_other),
        endgame_time,
        endgame_consistency,
        can_defend,
        can_resist_defense,
        maneuverability,
        ", ".join(programming_language),
        pathing,
        pinpoint,
        vision,
        apriltags,
        pid,
        ", ".join(other_software),
        drivetrain_reliability,
        intake_reliability,
        scoring_reliability,
        auto_reliability,
        endgame_reliability,
        ", ".join(known_problems),
        ", ".join(strengths),
        ", ".join(weaknesses),
        ", ".join(observed_strategy),
        comments
    ]

    try:
        worksheet = conectar_google_sheets()

        worksheet.append_row(
            scouting_data,
            value_input_option="USER_ENTERED"
        )

        st.success("Pit Scouting guardado correctamente en Google Sheets.")

    except Exception as e:
        st.error("No se pudo guardar el Pit Scouting.")
        st.exception(e)
