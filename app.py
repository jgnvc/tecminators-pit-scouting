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
    max-width: 720px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

.section-title {
    font-size: 22px;
    font-weight: 700;
    margin-top: 10px;
    margin-bottom: 8px;
}

.small-text {
    color: #999;
    font-size: 14px;
}

div[data-testid="stExpander"] {
    border-radius: 12px;
    margin-bottom: 10px;
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

st.markdown(
    '<div class="section-title">Información del equipo</div>',
    unsafe_allow_html=True
)

team_number = st.number_input(
    "Número de equipo",
    min_value=1,
    max_value=99999,
    step=1
)

team_name = st.text_input(
    "Nombre del equipo"
)

robot_name = st.text_input(
    "Nombre del robot"
)

scouter = st.text_input(
    "Scout"
)

photo = st.camera_input(
    "Foto del robot"
)


# =========================================================
# DRIVETRAIN
# =========================================================

with st.expander("1. Drivetrain", expanded=False):

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
        value=4
    )

    motor_type = st.selectbox(
        "Tipo de motor",
        [
            "REV HD Hex",
            "REV Core Hex",
            "Otro",
            "No sé"
        ]
    )

    drive_speed = st.slider(
        "Velocidad",
        1,
        5,
        3
    )

    acceleration = st.slider(
        "Aceleración",
        1,
        5,
        3
    )

    maneuverability = st.slider(
        "Maniobrabilidad",
        1,
        5,
        3
    )

    lateral_movement = st.checkbox(
        "Movimiento lateral"
    )

    rotation = st.checkbox(
        "Puede girar sobre su propio eje"
    )

    odometry = st.checkbox(
        "Usa odometría"
    )

    defense_resistance = st.slider(
        "Resistencia ante defensa",
        1,
        5,
        3
    )


# =========================================================
# AUTO
# =========================================================

with st.expander("2. AUTO", expanded=False):

    has_auto = st.checkbox(
        "Tiene autónomo"
    )

    auto_actions = st.multiselect(
        "Acciones de AUTO",
        [
            "Salir de la zona",
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

    auto_routes = st.number_input(
        "Número de rutas de AUTO",
        min_value=0,
        max_value=10,
        value=0
    )

    auto_time = st.selectbox(
        "Tiempo aproximado de AUTO",
        [
            "No sé",
            "0–5 s",
            "5–10 s",
            "10–15 s",
            "15+ s"
        ]
    )

    auto_consistency = st.slider(
        "Consistencia del AUTO",
        1,
        5,
        3
    )

    auto_vision = st.checkbox(
        "Usa visión en AUTO"
    )

    auto_apriltags = st.checkbox(
        "Usa AprilTags en AUTO"
    )

    auto_odometry = st.checkbox(
        "Usa odometría en AUTO"
    )


# =========================================================
# SCORING
# =========================================================

with st.expander("3. Scoring", expanded=False):

    scoring_capabilities = st.multiselect(
        "¿Qué puede hacer?",
        [
            "Hive Tips",
            "Pollen en Cell",
            "Nectar en Cell",
            "Pollen en Flowers",
            "Nectar en Flowers",
            "Bottom Nectar Bonus",
            "Pollen en Garden",
            "Nectar en Garden"
        ]
    )

    scoring_speed = st.slider(
        "Velocidad de scoring",
        1,
        5,
        3
    )

    cycle_time = st.selectbox(
        "Tiempo aproximado por ciclo",
        [
            "No sé",
            "< 2 s",
            "2–3 s",
            "3–4 s",
            "4–5 s",
            "5+ s"
        ]
    )

    can_score_moving = st.checkbox(
        "Puede hacer scoring mientras se mueve"
    )

    can_switch_elements = st.checkbox(
        "Puede cambiar rápidamente entre elementos"
    )

    scoring_consistency = st.slider(
        "Consistencia del scoring",
        1,
        5,
        3
    )


# =========================================================
# INTAKE
# =========================================================

with st.expander("4. Intake", expanded=False):

    has_intake = st.checkbox(
        "Tiene intake"
    )

    intake_elements = st.multiselect(
        "Elementos que puede recoger",
        [
            "Pollen",
            "Nectar",
            "Ambos"
        ]
    )

    intake_from_floor = st.checkbox(
        "Puede recoger desde el suelo"
    )

    intake_while_moving = st.checkbox(
        "Puede recoger mientras se mueve"
    )

    intake_speed = st.slider(
        "Velocidad del intake",
        1,
        5,
        3
    )

    intake_jams = st.selectbox(
        "¿Qué tan frecuente se atasca?",
        [
            "Nunca observado",
            "Raramente",
            "A veces",
            "Frecuentemente"
        ]
    )

    intake_consistency = st.slider(
        "Consistencia del intake",
        1,
        5,
        3
    )


# =========================================================
# FLOWERS / CELL / GARDEN
# =========================================================

with st.expander("5. Elementos de juego", expanded=False):

    st.markdown("### Cell")

    cell_capabilities = st.multiselect(
        "Capacidades en Cell",
        [
            "Pollen",
            "Nectar",
            "Ambos"
        ]
    )

    cell_capacity = st.number_input(
        "Capacidad aproximada en Cell",
        min_value=0,
        max_value=20,
        value=1
    )

    st.markdown("### Flowers")

    flower_capabilities = st.multiselect(
        "Capacidades en Flowers",
        [
            "Pollen",
            "Nectar",
            "Ambos"
        ]
    )

    bottom_bonus = st.checkbox(
        "Puede hacer Bottom Nectar Bonus"
    )

    st.markdown("### Garden")

    garden_capabilities = st.multiselect(
        "Capacidades en Garden",
        [
            "Pollen",
            "Nectar",
            "Ambos"
        ]
    )

    garden_capacity = st.number_input(
        "Capacidad aproximada en Garden",
        min_value=0,
        max_value=20,
        value=1
    )


# =========================================================
# HIVE TIPS
# =========================================================

with st.expander("6. Hive Tips", expanded=False):

    hive_tips = st.checkbox(
        "Puede hacer Hive Tips"
    )

    hive_method = st.selectbox(
        "Método",
        [
            "No aplica",
            "Mecanismo dedicado",
            "Drivetrain",
            "Otro",
            "No sé"
        ]
    )

    hive_speed = st.slider(
        "Velocidad de Hive Tips",
        1,
        5,
        3
    )

    hive_multiple = st.checkbox(
        "Puede hacer varios Hive Tips rápidamente"
    )

    hive_consistency = st.slider(
        "Consistencia",
        1,
        5,
        3
    )


# =========================================================
# MECANISMOS
# =========================================================

with st.expander("7. Mecanismos", expanded=False):

    mechanisms = st.multiselect(
        "Mecanismos observados",
        [
            "Intake",
            "Feeder",
            "Shooter",
            "Scorer",
            "Turret",
            "Lift",
            "Arm",
            "Wrist",
            "Claw",
            "Extensión",
            "Transfer",
            "Otro"
        ]
    )

    sensors = st.multiselect(
        "Sensores",
        [
            "Encoder",
            "IMU",
            "Pinpoint",
            "Color Sensor",
            "Distance Sensor",
            "Vision",
            "AprilTags",
            "Limelight",
            "Otro"
        ]
    )


# =========================================================
# END GAME
# =========================================================

with st.expander("8. End Game", expanded=False):

    endgame_park = st.checkbox(
        "Puede hacer Park"
    )

    endgame_mechanisms = st.multiselect(
        "Mecanismos de End Game",
        [
            "Hang",
            "Lift",
            "Extensión",
            "Arm",
            "Otro"
        ]
    )

    endgame_time = st.selectbox(
        "Tiempo aproximado",
        [
            "No realiza",
            "Más de 15 s",
            "10–15 s",
            "5–10 s",
            "Menos de 5 s"
        ]
    )

    endgame_consistency = st.slider(
        "Consistencia",
        1,
        5,
        3
    )


# =========================================================
# DEFENSA
# =========================================================

with st.expander("9. Defensa", expanded=False):

    can_defend = st.checkbox(
        "Puede jugar defensa"
    )

    defense_quality = st.slider(
        "Capacidad defensiva",
        1,
        5,
        3
    )

    can_escape = st.checkbox(
        "Puede escapar fácilmente de defensa"
    )

    can_block = st.checkbox(
        "Puede bloquear rutas"
    )


# =========================================================
# PROGRAMACIÓN
# =========================================================

with st.expander("10. Programación", expanded=False):

    programming = st.multiselect(
        "Software / herramientas",
        [
            "Java",
            "Blocks",
            "OnBot Java",
            "Pedro Pathing",
            "Road Runner",
            "FTCLib",
            "Pinpoint",
            "AprilTags",
            "OpenCV",
            "Limelight",
            "PID",
            "Feedforward",
            "Odometry",
            "Dashboard",
            "Otro"
        ]
    )

    autonomous_programs = st.number_input(
        "Número de autónomos programados",
        min_value=0,
        max_value=10,
        value=0
    )

    adjustable = st.checkbox(
        "Puede modificar parámetros rápidamente"
    )


# =========================================================
# CONFIABILIDAD
# =========================================================

with st.expander("11. Confiabilidad", expanded=False):

    drivetrain_reliability = st.slider(
        "Drivetrain",
        1,
        5,
        3
    )

    intake_reliability = st.slider(
        "Intake",
        1,
        5,
        3
    )

    scoring_reliability = st.slider(
        "Scoring",
        1,
        5,
        3
    )

    auto_reliability = st.slider(
        "AUTO",
        1,
        5,
        3
    )

    endgame_reliability = st.slider(
        "End Game",
        1,
        5,
        3
    )

    known_problems = st.multiselect(
        "Problemas observados",
        [
            "Drivetrain",
            "Intake",
            "Scoring",
            "AUTO",
            "End Game",
            "Sensores",
            "Software",
            "Ninguno"
        ]
    )


# =========================================================
# ESTRATEGIA
# =========================================================

with st.expander("12. Estrategia", expanded=False):

    primary_scoring = st.multiselect(
        "Scoring principal",
        [
            "Hive Tips",
            "Cell",
            "Flowers",
            "Garden"
        ]
    )

    secondary_scoring = st.multiselect(
        "Scoring secundario",
        [
            "Hive Tips",
            "Cell",
            "Flowers",
            "Garden",
            "End Game"
        ]
    )

    strategy_style = st.multiselect(
        "Estilo de juego",
        [
            "Alta velocidad",
            "Alta consistencia",
            "Scoring",
            "Defensa",
            "Contra-defensa",
            "End Game"
        ]
    )

    alliance_value = st.multiselect(
        "¿Qué aporta a una alianza?",
        [
            "Scoring",
            "AUTO",
            "Defensa",
            "Contra-defensa",
            "End Game",
            "Consistencia"
        ]
    )


# =========================================================
# EVALUACIÓN GENERAL
# =========================================================

with st.expander("13. Evaluación general", expanded=False):

    overall_speed = st.slider(
        "Velocidad general",
        1,
        5,
        3
    )

    overall_scoring = st.slider(
        "Scoring general",
        1,
        5,
        3
    )

    overall_auto = st.slider(
        "AUTO general",
        1,
        5,
        3
    )

    overall_endgame = st.slider(
        "End Game general",
        1,
        5,
        3
    )

    overall_defense = st.slider(
        "Defensa general",
        1,
        5,
        3
    )

    overall_reliability = st.slider(
        "Confiabilidad general",
        1,
        5,
        3
    )

    overall_consistency = st.slider(
        "Consistencia general",
        1,
        5,
        3
    )


# =========================================================
# COMENTARIOS
# =========================================================

with st.expander("14. Comentarios", expanded=True):

    comments = st.text_area(
        "Observaciones",
        placeholder="Escribe cualquier información importante..."
    )


# =========================================================
# GUARDAR
# =========================================================

st.markdown("---")

if st.button(
    "GUARDAR PIT SCOUTING",
    type="primary",
    use_container_width=True
):

    if team_number <= 0:
        st.error("Ingresa un número de equipo.")
        st.stop()

    row = [
        team_number,
        team_name,
        robot_name,
        scouter,

        bool(photo),

        drivetrain,
        drive_motors,
        motor_type,
        drive_speed,
        acceleration,
        maneuverability,
        lateral_movement,
        rotation,
        odometry,
        defense_resistance,

        has_auto,
        ", ".join(auto_actions),
        auto_routes,
        auto_time,
        auto_consistency,
        auto_vision,
        auto_apriltags,
        auto_odometry,

        ", ".join(scoring_capabilities),
        scoring_speed,
        cycle_time,
        can_score_moving,
        can_switch_elements,
        scoring_consistency,

        has_intake,
        ", ".join(intake_elements),
        intake_from_floor,
        intake_while_moving,
        intake_speed,
        intake_jams,
        intake_consistency,

        ", ".join(cell_capabilities),
        cell_capacity,
        ", ".join(flower_capabilities),
        bottom_bonus,
        ", ".join(garden_capabilities),
        garden_capacity,

        hive_tips,
        hive_method,
        hive_speed,
        hive_multiple,
        hive_consistency,

        ", ".join(mechanisms),
        ", ".join(sensors),

        endgame_park,
        ", ".join(endgame_mechanisms),
        endgame_time,
        endgame_consistency,

        can_defend,
        defense_quality,
        can_escape,
        can_block,

        ", ".join(programming),
        autonomous_programs,
        adjustable,

        drivetrain_reliability,
        intake_reliability,
        scoring_reliability,
        auto_reliability,
        endgame_reliability,
        ", ".join(known_problems),

        ", ".join(primary_scoring),
        ", ".join(secondary_scoring),
        ", ".join(strategy_style),
        ", ".join(alliance_value),

        overall_speed,
        overall_scoring,
        overall_auto,
        overall_endgame,
        overall_defense,
        overall_reliability,
        overall_consistency,

        comments
    ]

    try:
        worksheet = conectar_google_sheets()

        worksheet.append_row(
            row,
            value_input_option="USER_ENTERED"
        )

        st.success("Pit Scouting guardado correctamente.")

    except Exception as e:
        st.error("No se pudo guardar el scouting.")
        st.exception(e)
