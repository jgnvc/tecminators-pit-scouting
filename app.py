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
    step=1,
    key="team_number"
)

team_name = st.text_input(
    "Nombre del equipo",
    key="team_name"
)

robot_name = st.text_input(
    "Nombre del robot",
    key="robot_name"
)

scouter = st.text_input(
    "Scout",
    key="scouter"
)


# =========================================================
# 1. DRIVETRAIN
# =========================================================

with st.expander("1. Drivetrain", expanded=False):

    drivetrain = st.selectbox(
        "Tipo de drivetrain",
        [
            "Mecanum",
            "Tank",
            "X-Drive",
            "Otro"
        ],
        key="drivetrain"
    )

    drive_motors = st.number_input(
        "Número de motores",
        min_value=0,
        max_value=8,
        value=4,
        key="drive_motors"
    )

    motor_type = st.selectbox(
        "Tipo de motor",
        [
            "REV HD Hex",
            "REV Core Hex",
            "Otro",
            "No sé"
        ],
        key="motor_type"
    )

    drive_speed = st.slider(
        "Velocidad",
        1,
        5,
        3,
        key="drive_speed"
    )

    acceleration = st.slider(
        "Aceleración",
        1,
        5,
        3,
        key="acceleration"
    )

    maneuverability = st.slider(
        "Maniobrabilidad",
        1,
        5,
        3,
        key="maneuverability"
    )

    lateral_movement = st.checkbox(
        "Movimiento lateral",
        key="lateral_movement"
    )

    rotation = st.checkbox(
        "Puede girar sobre su propio eje",
        key="rotation"
    )

    odometry = st.checkbox(
        "Usa odometría",
        key="odometry"
    )

    defense_resistance = st.slider(
        "Resistencia ante defensa",
        1,
        5,
        3,
        key="defense_resistance"
    )


# =========================================================
# 2. AUTO
# =========================================================

with st.expander("2. AUTO", expanded=False):

    has_auto = st.checkbox(
        "Tiene autónomo",
        key="has_auto"
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
        ],
        key="auto_actions"
    )

    auto_routes = st.number_input(
        "Número de rutas de AUTO",
        min_value=0,
        max_value=10,
        value=0,
        key="auto_routes"
    )

    auto_time = st.selectbox(
        "Tiempo aproximado de AUTO",
        [
            "No sé",
            "0–5 s",
            "5–10 s",
            "10–15 s",
            "15+ s"
        ],
        key="auto_time"
    )

    auto_consistency = st.slider(
        "Consistencia del AUTO",
        1,
        5,
        3,
        key="auto_consistency"
    )

    auto_vision = st.checkbox(
        "Usa visión en AUTO",
        key="auto_vision"
    )

    auto_apriltags = st.checkbox(
        "Usa AprilTags en AUTO",
        key="auto_apriltags"
    )

    auto_odometry = st.checkbox(
        "Usa odometría en AUTO",
        key="auto_odometry"
    )


# =========================================================
# 3. SCORING
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
        ],
        key="scoring_capabilities"
    )

    scoring_speed = st.slider(
        "Velocidad de scoring",
        1,
        5,
        3,
        key="scoring_speed"
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
        ],
        key="cycle_time"
    )

    can_score_moving = st.checkbox(
        "Puede hacer scoring mientras se mueve",
        key="can_score_moving"
    )

    can_switch_elements = st.checkbox(
        "Puede cambiar rápidamente entre elementos",
        key="can_switch_elements"
    )

    scoring_consistency = st.slider(
        "Consistencia del scoring",
        1,
        5,
        3,
        key="scoring_consistency"
    )


# =========================================================
# 4. INTAKE
# =========================================================

with st.expander("4. Intake", expanded=False):

    has_intake = st.checkbox(
        "Tiene intake",
        key="has_intake"
    )

    intake_elements = st.multiselect(
        "Elementos que puede recoger",
        [
            "Pollen",
            "Nectar",
            "Ambos"
        ],
        key="intake_elements"
    )

    intake_from_floor = st.checkbox(
        "Puede recoger desde el suelo",
        key="intake_from_floor"
    )

    intake_while_moving = st.checkbox(
        "Puede recoger mientras se mueve",
        key="intake_while_moving"
    )

    intake_speed = st.slider(
        "Velocidad del intake",
        1,
        5,
        3,
        key="intake_speed"
    )

    intake_jams = st.selectbox(
        "¿Qué tan frecuente se atasca?",
        [
            "Nunca observado",
            "Raramente",
            "A veces",
            "Frecuentemente"
        ],
        key="intake_jams"
    )

    intake_consistency = st.slider(
        "Consistencia del intake",
        1,
        5,
        3,
        key="intake_consistency"
    )


# =========================================================
# 5. ELEMENTOS DE JUEGO
# =========================================================

with st.expander("5. Elementos de juego", expanded=False):

    st.markdown("### Cell")

    cell_capabilities = st.multiselect(
        "Capacidades en Cell",
        [
            "Pollen",
            "Nectar",
            "Ambos"
        ],
        key="cell_capabilities"
    )

    cell_capacity = st.number_input(
        "Capacidad aproximada en Cell",
        min_value=0,
        max_value=20,
        value=1,
        key="cell_capacity"
    )

    st.markdown("### Flowers")

    flower_capabilities = st.multiselect(
        "Capacidades en Flowers",
        [
            "Pollen",
            "Nectar",
            "Ambos"
        ],
        key="flower_capabilities"
    )

    bottom_bonus = st.checkbox(
        "Puede hacer Bottom Nectar Bonus",
        key="bottom_bonus"
    )

    st.markdown("### Garden")

    garden_capabilities = st.multiselect(
        "Capacidades en Garden",
        [
            "Pollen",
            "Nectar",
            "Ambos"
        ],
        key="garden_capabilities"
    )

    garden_capacity = st.number_input(
        "Capacidad aproximada en Garden",
        min_value=0,
        max_value=20,
        value=1,
        key="garden_capacity"
    )


# =========================================================
# 6. HIVE TIPS
# =========================================================

with st.expander("6. Hive Tips", expanded=False):

    hive_tips = st.checkbox(
        "Puede hacer Hive Tips",
        key="hive_tips"
    )

    hive_method = st.selectbox(
        "Método",
        [
            "No aplica",
            "Mecanismo dedicado",
            "Drivetrain",
            "Otro",
            "No sé"
        ],
        key="hive_method"
    )

    hive_speed = st.slider(
        "Velocidad de Hive Tips",
        1,
        5,
        3,
        key="hive_speed"
    )

    hive_multiple = st.checkbox(
        "Puede hacer varios Hive Tips rápidamente",
        key="hive_multiple"
    )

    hive_consistency = st.slider(
        "Consistencia de Hive Tips",
        1,
        5,
        3,
        key="hive_consistency"
    )


# =========================================================
# 7. MECANISMOS
# =========================================================

with st.expander("7. Mecanismos", expanded=False):

    st.markdown("### Mecanismos del robot")

    chassis = st.checkbox(
        "Chassis",
        key="mechanism_chassis"
    )

    intake = st.checkbox(
        "Intake",
        key="mechanism_intake"
    )

    feeder = st.checkbox(
        "Feeder",
        key="mechanism_feeder"
    )

    shooter = st.checkbox(
        "Shooter",
        key="mechanism_shooter"
    )

    has_other_mechanism = st.radio(
        "¿Tiene otro mecanismo?",
        [
            "No",
            "Sí"
        ],
        horizontal=True,
        key="has_other_mechanism"
    )

    if has_other_mechanism == "Sí":

        other_mechanism = st.text_input(
            "Nombre del otro mecanismo",
            placeholder="Ej. Turret",
            key="other_mechanism_text"
        )

    else:

        other_mechanism = ""

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
        ],
        key="sensors"
    )


# =========================================================
# 8. END GAME
# =========================================================

with st.expander("8. End Game", expanded=False):

    endgame_park = st.checkbox(
        "Puede hacer Park",
        key="endgame_park"
    )

    endgame_mechanisms = st.multiselect(
        "Mecanismos de End Game",
        [
            "Hang",
            "Lift",
            "Extensión",
            "Arm",
            "Otro"
        ],
        key="endgame_mechanisms"
    )

    endgame_time = st.selectbox(
        "Tiempo aproximado",
        [
            "No realiza",
            "Más de 15 s",
            "10–15 s",
            "5–10 s",
            "Menos de 5 s"
        ],
        key="endgame_time"
    )

    endgame_consistency = st.slider(
        "Consistencia del End Game",
        1,
        5,
        3,
        key="endgame_consistency"
    )


# =========================================================
# 9. DEFENSA
# =========================================================

with st.expander("9. Defensa", expanded=False):

    can_defend = st.checkbox(
        "Puede jugar defensa",
        key="can_defend"
    )

    defense_quality = st.slider(
        "Capacidad defensiva",
        1,
        5,
        3,
        key="defense_quality"
    )

    can_escape = st.checkbox(
        "Puede escapar fácilmente de defensa",
        key="can_escape"
    )

    can_block = st.checkbox(
        "Puede bloquear rutas",
        key="can_block"
    )


# =========================================================
# 10. PROGRAMACIÓN
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
        ],
        key="programming"
    )

    autonomous_programs = st.number_input(
        "Número de autónomos programados",
        min_value=0,
        max_value=10,
        value=0,
        key="autonomous_programs"
    )

    adjustable = st.checkbox(
        "Puede modificar parámetros rápidamente",
        key="adjustable"
    )


# =========================================================
# 11. CONFIABILIDAD
# =========================================================

with st.expander("11. Confiabilidad", expanded=False):

    drivetrain_reliability = st.slider(
        "Drivetrain",
        1,
        5,
        3,
        key="drivetrain_reliability"
    )

    intake_reliability = st.slider(
        "Intake",
        1,
        5,
        3,
        key="intake_reliability"
    )

    scoring_reliability = st.slider(
        "Scoring",
        1,
        5,
        3,
        key="scoring_reliability"
    )

    auto_reliability = st.slider(
        "AUTO",
        1,
        5,
        3,
        key="auto_reliability"
    )

    endgame_reliability = st.slider(
        "End Game",
        1,
        5,
        3,
        key="endgame_reliability"
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
        ],
        key="known_problems"
    )


# =========================================================
# 12. ESTRATEGIA
# =========================================================

with st.expander("12. Estrategia", expanded=False):

    primary_scoring = st.multiselect(
        "Scoring principal",
        [
            "Hive Tips",
            "Cell",
            "Flowers",
            "Garden"
        ],
        key="primary_scoring"
    )

    secondary_scoring = st.multiselect(
        "Scoring secundario",
        [
            "Hive Tips",
            "Cell",
            "Flowers",
            "Garden",
            "End Game"
        ],
        key="secondary_scoring"
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
        ],
        key="strategy_style"
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
        ],
        key="alliance_value"
    )


# =========================================================
# 13. EVALUACIÓN GENERAL
# =========================================================

with st.expander("13. Evaluación general", expanded=False):

    overall_speed = st.slider(
        "Velocidad general",
        1,
        5,
        3,
        key="overall_speed"
    )

    overall_scoring = st.slider(
        "Scoring general",
        1,
        5,
        3,
        key="overall_scoring"
    )

    overall_auto = st.slider(
        "AUTO general",
        1,
        5,
        3,
        key="overall_auto"
    )

    overall_endgame = st.slider(
        "End Game general",
        1,
        5,
        3,
        key="overall_endgame"
    )

    overall_defense = st.slider(
        "Defensa general",
        1,
        5,
        3,
        key="overall_defense"
    )

    overall_reliability = st.slider(
        "Confiabilidad general",
        1,
        5,
        3,
        key="overall_reliability"
    )

    overall_consistency = st.slider(
        "Consistencia general",
        1,
        5,
        3,
        key="overall_consistency"
    )


# =========================================================
# 14. COMENTARIOS
# =========================================================

with st.expander("14. Comentarios", expanded=True):

    comments = st.text_area(
        "Observaciones",
        placeholder="Escribe cualquier información importante...",
        key="comments"
    )


# =========================================================
# FOTO DEL ROBOT
# =========================================================

st.markdown("---")

st.markdown(
    '<div class="section-title">Foto del Robot</div>',
    unsafe_allow_html=True
)

photo_method = st.radio(
    "¿Cómo quieres agregar la foto?",
    [
        "No agregar foto",
        "Adjuntar foto",
        "Tomar foto"
    ],
    horizontal=True,
    key="photo_method"
)

robot_photo = None

if photo_method == "Adjuntar foto":

    robot_photo = st.file_uploader(
        "Adjuntar foto del robot",
        type=[
            "jpg",
            "jpeg",
            "png"
        ],
        key="robot_photo_upload"
    )

elif photo_method == "Tomar foto":

    robot_photo = st.camera_input(
        "Tomar foto del robot",
        key="robot_camera"
    )


# =========================================================
# GUARDAR
# =========================================================

st.markdown("---")

if st.button(
    "GUARDAR PIT SCOUTING",
    type="primary",
    use_container_width=True,
    key="save_pit_scouting"
):

    if team_number <= 0:

        st.error(
            "Ingresa un número de equipo."
        )

        st.stop()


    # =====================================================
    # MECANISMOS
    # =====================================================

    mechanisms_final = []

    if chassis:
        mechanisms_final.append("Chassis")

    if intake:
        mechanisms_final.append("Intake")

    if feeder:
        mechanisms_final.append("Feeder")

    if shooter:
        mechanisms_final.append("Shooter")

    if has_other_mechanism == "Sí" and other_mechanism.strip():

        mechanisms_final.append(
            f"Otro: {other_mechanism.strip()}"
        )


    # =====================================================
    # FILA PARA GOOGLE SHEETS
    # =====================================================

    row = [

        # Información
        team_number,
        team_name,
        robot_name,
        scouter,

        # Drivetrain
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

        # AUTO
        has_auto,
        ", ".join(auto_actions),
        auto_routes,
        auto_time,
        auto_consistency,
        auto_vision,
        auto_apriltags,
        auto_odometry,

        # Scoring
        ", ".join(scoring_capabilities),
        scoring_speed,
        cycle_time,
        can_score_moving,
        can_switch_elements,
        scoring_consistency,

        # Intake
        has_intake,
        ", ".join(intake_elements),
        intake_from_floor,
        intake_while_moving,
        intake_speed,
        intake_jams,
        intake_consistency,

        # Elementos de juego
        ", ".join(cell_capabilities),
        cell_capacity,
        ", ".join(flower_capabilities),
        bottom_bonus,
        ", ".join(garden_capabilities),
        garden_capacity,

        # Hive Tips
        hive_tips,
        hive_method,
        hive_speed,
        hive_multiple,
        hive_consistency,

        # Mecanismos
        ", ".join(mechanisms_final),
        ", ".join(sensors),

        # End Game
        endgame_park,
        ", ".join(endgame_mechanisms),
        endgame_time,
        endgame_consistency,

        # Defensa
        can_defend,
        defense_quality,
        can_escape,
        can_block,

        # Programación
        ", ".join(programming),
        autonomous_programs,
        adjustable,

        # Confiabilidad
        drivetrain_reliability,
        intake_reliability,
        scoring_reliability,
        auto_reliability,
        endgame_reliability,
        ", ".join(known_problems),

        # Estrategia
        ", ".join(primary_scoring),
        ", ".join(secondary_scoring),
        ", ".join(strategy_style),
        ", ".join(alliance_value),

        # Evaluación general
        overall_speed,
        overall_scoring,
        overall_auto,
        overall_endgame,
        overall_defense,
        overall_reliability,
        overall_consistency,

        # Comentarios
        comments,

        # Foto
        "Sí" if robot_photo else "No"
    ]


    # =====================================================
    # GUARDAR EN GOOGLE SHEETS
    # =====================================================

    try:

        worksheet = conectar_google_sheets()

        worksheet.append_row(
            row,
            value_input_option="USER_ENTERED"
        )

        st.success(
            "Pit Scouting guardado correctamente."
        )

    except Exception as e:

        st.error(
            "No se pudo guardar el scouting."
        )

        st.exception(e)
