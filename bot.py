
import es
import est
import playerlib
import gamethread
import random
import spe
from spe import HookAction
from spe import HookType
from spe.tools.player import SPEPlayer
import esc
import popuplib
import usermsg
import repeat
import vecmath
import cmdlib
import keyvalues
import os
import time
import votelib
import msglib
import math

import zeisen_story

def _getEyeAngle():
	return 'CCSPlayer.m_angEyeAngles[%s]'
_eyeangle = _getEyeAngle()

sv = es.ServerVar
OFFSET_MODEL_NAME = 516 if os.name == 'nt' else 536 # 2014.2.14 IDA FREE (Zeisen)
OFFSET_CLAN_TAG = 5580 if spe.platform == 'nt' else 5600 # 2014.2.10 IDA Free (Zeisen)
MAX_SIZE        = 16
SPECIAL_MAPS = ["de_train", "de_colors"]
REST_MAPS = ["de_nightfever", "de_rush_v2"]

BAN_LIST = ["KKK",
"LASD"]

NORMAL_WORLD = ["de_nightfever",
"cs_assault2_goban_b3",
"de_aztec",
"de_piranesi",
"de_aos_monkey_s1",
]

FAIRY_WORLD = ["de_inferno",
"cs_calm_pro",
"de_sa_cargo",
"de_dust2_mariostyle",
]

MONSTER_WORLD = ["cs_Wolfenstein_ur_beta",
"cs_complex",
"de_bluecorridor_kai",
"de_museum_remake_b6",
"de_inferno_pro",
]

ICE_WORLD = ["cs_frozen"]

WEAPON_BOT = (
"[Unknown] Crizi",
"[Human] 퀘이사",
"[Human] 레일라",
"[Human] 던 레이트",
"[Human] 마트 루핀",
"[Human] 스트레이트 킹",
"[Extra] 오오타 준페이",
)

_healthprop = "CBasePlayer.m_iHealth"
_armorprop = "CCSPlayer.m_ArmorValue"
_blockprop = "CCSPlayer.baseclass.baseclass.baseclass.baseclass.baseclass.baseclass.m_CollisionGroup"
_speedprop = "CBasePlayer.localdata.m_flLaggedMovementValue"
_moneyprop = "CCSPlayer.m_iAccount"
_movetype = "CBaseEntity.movetype"

BOT_LIST = {
	'[Normal]': {
		'damage': 20,
		'damage_slow': 1,
		'damage_slow': 1,
	},
}

SERVER_UNLOCK_LIST = {
	'de_train': {
		'unlock_info': "레벨 30 달성",
	},
	'de_dust2_mariostyle': {
		'unlock_info': '스토리 프롤로그 클리어',
	},
}

_hoo_LIST = {
	'npc_custom_nightfever': {
		'npc_name': '#255,255,255레아',
		'npc_rain_chat': ["비... 비라니! 이번 스케줄이!"],
		'npc_chat': ["안녕하세요, 레아 라고 합니다!"],
		'npc_popup': "-1",
		'npc_info': "＊ 레아\n \n대표 어빌리티는 인기. 인기도가 약 1억정도..\n아이돌 코드를 지니고있다.",
		'npc_xp': 0,
		'npc_negative_msg': ["N"],
	},
	'npc_inventor_nightfever': {
		'npc_name': '#255,255,255렉스',
		'npc_rain_chat': ["원래 비는 되게 위험했어야 해. 추락 속도로 힘이 다르거든. 그런데 공기 저항때문에 ..."],
		'npc_chat': ["좋아, 이번에도 흥미로운걸 들고왔지!", "하하하하! 대단하구나!"],
		'npc_popup': "inventor_shop_1",
		'npc_info': "＊ 렉스\n \n아이템을 발명하는 과학자다. 성격은 미쳐있지만. 나름 괜찮은 사람이라고 볼수있다.\n하지만 그는 잘때도, 일할때도 저 옷만을 입는다고 한다..",
		'npc_xp': 0,
		'npc_negative_msg': ["N"],
	},
	'npc_world_nightfever': {
		'npc_name': '#255,255,255베닉스',
		'npc_rain_chat': ["음..."],
		'npc_chat': ["이 월드 투어는 아침에만 운행합니다.", "월드 투어중 사망은 책임지지 않습니다."],
		'npc_popup': "world_start",
		'npc_info': "＊ 베닉스\n \n다른 월드로 이동하는데 도움을 주는 NPC이다. 하지만... 조심하자.",
		'npc_xp': 0,
		'npc_negative_msg': ["N"],
	},
	'npc_ticket_nightfever': {
		'npc_name': '#255,255,255Gamble A Type',
		'npc_rain_chat': ["GAMBLE!!!"],
		'npc_chat': ["GAMBLE!!!"],
		'npc_popup': "gamble_start",
		'npc_info': "＊ Gamble A Type\n \nㅅㅂ 이건 뭐야",
		'npc_xp': 0,
		'npc_negative_msg': ["N"],
	},
	'npc_robot1_nightfever': {
		'npc_name': '#255,255,255Robot',
		'npc_rain_chat': ["비를 즐기고 싶다고 전합니다...", "... 비가 오는 기분은 마치 개가 흰 눈이 내리는걸 보며 즐거워하는겁니다."],
		'npc_chat': ["...안녕하세요, 반갑습니다.", "... 봉사는 적당히 합니다."],
		'npc_popup': "-1",
		'npc_info': "＊ Robot(A Type)\n \n대표 어빌리티는 없다. 이 로봇 AI는 정신지체를 가지고있다.",
		'npc_xp': 0,
		'npc_negative_msg': ["N"],
	},
	'npc_reisen_nightfever': {
		'npc_name': '#0,0,255레이센',
		'npc_rain_chat': ["비... 인가요, 축축해져서 싫은데...", "으으.. 오싹오싹해.."],
		'npc_chat': ["알바하러 가야될 시간인데... 가긴 좀 싫네요.", "다들 바쁘지만 언젠간 한 자리에 모이겠죠?"],
		'npc_popup': "-1",
		'npc_info': "＊ 레이센\n \n그녀의 대표 어빌리티는 소심. 편의점 아르바이트를 하고 있다고 한다.",
		'npc_xp': 1000,
		'npc_negative_msg': ["당신은... 안됩니다.", "시... 싫어! 저리 가요!"],
	},
	'npc_tenji_nightfever': {
		'npc_name': '#255,0,0텐지',
		'npc_rain_chat': ["흠, 비인가.  눈감고 듣기에 딱 좋군.", "비가 오더라도 이 주점의 인기는 멈추지 않지."],
		'npc_chat': ["편안히 즐기게, 그게 가장 황혼주점을 가장 재미있게 즐기는 방법이라고.", "언제나 오게, 기다리고 있을거야."],
		'npc_popup': "-1",
		'npc_info': "＊ 아마카스 바레이 텐지\n \n그의 대표 어빌리티는 여유이다. 황혼주점의 점장. 요리, 춤 모든게 뛰어나다.",
		'npc_xp': 0,
	},
	'npc_junpei_nightfever': {
		'npc_name': '#255,255,255오오타 준페이',
		'npc_rain_chat': ["젠장 비잖아. 우산 안가지고 왔다고!", "이럴수가... 돌아가는 길은 어쩌지..."],
		'npc_chat': ["일 났다... 막차인데 늦겠어...", "좋았어! 오늘은 거하게 즐겨보자고!", "옆에 있는곳은 신경 꺼. 점장이 냅두고 있는거 같지만... 아주 게이들 살판 났네.", "정말로 사회 생활 적응하기 힘들구나..."],
		'npc_popup': "-1",
		'npc_info': "＊ 오오타 준페이\n \n그의 대표 어빌리티는 끈기이다. 가끔 서버 이벤트 맵에서 엑스트라로 출현한다.\n황혼주점을 즐겨오는 셀러리맨.",
		'npc_xp': 0,
	},
	'npc_sonic_nightfever': {
		'npc_name': 'Sonic',
		'npc_rain_chat': ["비는 루나가 좋아하곤 했었죠.", "황혼주점 안에서 빗소리를 즐겨보세요. 좋지 않은가요?"],
		'npc_chat': ["여기 전부 모이시면 이동시켜 드릴수 있어요.", "가실까요?", "루나는 어떻게 지내고 있을까..."],
		'npc_popup': "-1",
		'npc_info': "＊ Sonic\n \n그는 대표 어빌리티로 광역 텔레포트가 있다.\n자신이 그 위치를 외우면 나중에 그 곳으로 텔레포트가 가능하다고 하다는 이야기가 있다.\n \n아직 그에 대해 정확히는 알려진 바 없다.",
		'npc_xp': 0,
	},
	'npc_gaygate_nightfever': {
		'npc_name': '???',
		'npc_rain_chat': ["여기는 비가 오더라도 즐길수 있다고, #0,0,255Boy♂"],
		'npc_chat': ["#pink핑크색 티켓#255,255,255을 가지고 오라고, #0,0,255Boy♂"],
		'npc_popup': "-1",
		'npc_info': "＊ ???\n \n알수없는 곳의 문지기 역할을 하는 사람. 아무래도 안으로 들어가면 안될거같다..\n \n저 곳을 갈려면 핑크색 티켓이 필요하다는데...",
		'npc_xp': 0,
	},
}

SOUNDTRACK_LIST = {
	'de_sa_cargo': {
		'album': "東方リズムカ-ニバル！紅 ORIGINAL SOUND TRACK",
		'artist': "FocasLens (紫苑)",
	},
	'cs_calm_pro': {
		'album': "大空魔術　～ Magical Astronomy",
		'artist': "上海アリス幻樂團 (ZUN)",
	},
	'de_colors': {
		'album': " ",
		'artist': " ",
	},
	'de_inferno_pro': {
		'album': "All Remix",
		'artist': "All Remix",
	},
	'de_nightfever_battle': {
		'album': "Unknown",
		'artist': "07th Expansion",
	},
	'de_rush_v2': {
		'album': "Unknown",
		'artist': "07th Expansion",
	},
	'de_nightfever': {
		'album': "Unknown",
		'artist': "AQUASTYLE (豊田竜行)",
	},
	'cs_assault2_goban_b3': {
		'album': "妖々剣戟夢想 オリジナルサウンドトラック",
		'artist': "sound sepher (Jun.A)",
	},
	'de_inferno': {
		'album': "東方風神錄　～ Mountain of Faith",
		'artist': "上海アリス幻樂團 (ZUN)",
	},
	'de_museum_remake_b6': {
		'album': "東方紅魔鄕　～ the Embodiment of Scarlet Devil",
		'artist': "上海アリス幻樂團 (ZUN)",
	},
	'de_cbble': {
		'album': "東方靈異傳　～ Highly Responsive to Prayers",
		'artist': "上海アリス幻樂團 (ZUN)",
	},
	'de_aos_monkey_s1': {
		'album': "夢違科學世紀　～ Changeability of Strange Dream",
		'artist': "上海アリス幻樂團 (ZUN)",
	},
	'de_dust2_mariostyle': {
		'album': 'Kamilia/COOL&CREATE Soundtrack',
		'artist': "Kamilia/COOL&CREATE",
	},
	'cs_complex': {
		'album': "Geometry Dash Soundtrack",
		'artist': "Newgrounds",
	},
	'de_bluecorridor_kai': {
		'album': "東方萃夢想　～ Immaterial and Missing Power",
		'artist': "上海アリス幻樂團 (ZUN)",
	},
	'de_fedra_autumn': {
		'album': "秋満開の風に舞う",
		'artist': "ばんばんしー",
	},
	'de_train': {
		'album': "東方臑茶魔　～ The Acquaintance Of My Daddy",
		'artist': "NicoNicoDouga (Samidare)",
	},
	'de_westwood_2010': {
		'album': "BlazBlue Continuum Shift Soundtrack",
		'artist': "Arc System Works Co., Ltd.",
	},
	'de_aztec': {
		'album': "東方永夜抄　～ Imperishable Night",
		'artist': "上海アリス幻樂團 (ZUN)",
	},
	'de_piranesi': {
		'album': "東方妖妖夢　～ Perfect Cherry Blossom",
		'artist': "上海アリス幻樂團 (ZUN)",
	},
	'cs_italy': {
		'album': "黃昏酒場 ~ Uwabami Breakers",
		'artist': "呑んべぇ會",
	},
	'cs_Wolfenstein_ur_beta': {
		'album': "The Binding of Isaac Soundtrack",
		'artist': "Danny Baranowsky",
	},
}

UNLOCK_LIST = {
	'Jumper': {
		'unlock': "unlock_1",
		'unlock_info': "#gold누적 점프 10000번을 달성#255,255,255하면 이 스킬을 언락할수 있습니다!",
	},
	'Clutterfunk': {
		'unlock': "unlock_2",
		'unlock_info': "#255,0,0[Gunner] Elite Hunter를 사살#255,255,255하면 이 아이템을 언락할수 있습니다!\n#purple출현 맵 : ???",
	},
	'Be Soldier AR': {
		'unlock': "unlock_3",
		'unlock_info': "#goldcs_complex 맵에서 M4A1 무기로 누적 1000번 사살#255,255,255하면 아이템을 언락할수 있습니다!",
	},
	'Be Soldier SR': {
		'unlock': "unlock_4",
		'unlock_info': "#125,125,125de_inferno_pro 맵에서 SCOUT, AWP 무기로 누적 1000번 사살#255,255,255하면 아이템을 언락할수 있습니다!",
	},
	'Magic Show': {
		'unlock': "unlock_5",
		'unlock_info': "#255,0,0[Magician] White Bird를 사살#255,255,255하면 이 아이템을 언락할수 있습니다!\n#purple출현 맵 : ???",
	},
}

ITEM_LIST = {
	0: {
		'name': "money",
		'showname': "엔",
		'info': "일본의 화폐.",
		'effect_info': "... 쓰기 나름.",
		'trade': 1,
		'allow_use': 0,
	},
	1: {
		'name': "item1",
		'showname': "경찰봉",
		'info': "경찰을 위해 만들어진 무기?",
		'effect_info': "사용할경우 마켓에서 칼넉백 가능",
		'trade': 1,
		'allow_use': 0,
	},
	2: {
		'name': "item2",
		'showname': "화이트 버드의 초대장",
		'info': "깜찍하고 끔찍하고 아름다운 공연장으로 당신을 초대합니다! - 매지션 曰",
		'effect_info': "이벤트 월드(매지션)로 변경합니다.",
		'trade': 1,
		'allow_use': 0,
	},
	3: {
		'name': "item3",
		'showname': "몬스터 투어 티켓",
		'info': "세계를 여행하세요!",
		'effect_info': "몬스터 월드로 변경합니다.",
		'trade': 1,
		'allow_use': 1,
	},
	4: {
		'name': "item4",
		'showname': "부품 Type A",
		'info': "Shooter에게서 얻을수 있는 부품.",
		'effect_info': "...",
		'trade': 1,
		'allow_use': 0,
	},
	5: {
		'name': "item5",
		'showname': "파란색 물약",
		'info': "과학자들이 발명한 파란색 물약이다.",
		'effect_info': "아이템을 사용할경우 확률로 스텟이 초기화됩니다.",
		'trade': 1,
		'allow_use': 1,
	},
	6: {
		'name': "item6",
		'showname': "보라색 물약",
		'info': "과학자들이 발명한 보라색 물약이다.",
		'effect_info': "아이템을 사용할경우 확률로 스킬이 초기화됩니다.",
		'trade': 1,
		'allow_use': 1,
	},
	7: {
		'name': "item7",
		'showname': "페어리 투어 티켓",
		'info': "세계를 여행하세요!",
		'effect_info': "페어리 월드로 변경합니다.",
		'trade': 1,
		'allow_use': 0,
	},
	8: {
		'name': "item8",
		'showname': "좀비 샘플",
		'info': "Normal에게서 얻을수 있는 샘플.",
		'effect_info': "...",
		'trade': 1,
		'allow_use': 0,
	},
	9: {
		'name': "item9",
		'showname': "요정의 찢어진 날개",
		'info': "Flaght에게서 얻을수 있는 샘플.",
		'effect_info': "...",
		'trade': 1,
		'allow_use': 0,
	},
}

SKILL_TEST_PRINT = (
"Health+",
"Remote Human Upgrade",
"Magic Bullet",
"Jumper",
"Crazing Air Knife",
)

SKILL_TEST = {
	'Health+': {
		'skillname': "skill1",
		'need_skillp': 2,
		'max': 10,
		'skillbook': -1,
		'info': '체력을 증진시켜줍니다. ',
		'level_info': '익힐때 마다 체력이 15씩 증진합니다.',
		'nope_skill': ["none"],
		'need_level': 1,
	},
	'Remote Human Upgrade': {
		'skillname': "skill2",
		'need_skillp': 5,
		'max': 1,
		'skillbook': -1,
		'info': '익히면 Remote Human을 구매했을 때, 스폰된 아군 봇들이 당신에게로 스폰됩니다.',
		'level_info': '(한번만 익히는 스킬입니다.)',
		'nope_skill': ["none"],
		'need_level': 10,
	},
	'Magic Bullet': {
		'skillname': "skill3",
		'need_skillp': 1,
		'max': 5,
		'skillbook': -1,
		'info': '마지막 탄알의 데미지가 상승합니다.',
		'level_info': '익힐때 마다 효과 데미지가 20％ 상승합니다.',
		'nope_skill': ["none"],
		'need_level': 3,
	},
	'Jumper': {
		'skillname': "skill4",
		'need_skillp': 5,
		'max': 1,
		'skillbook': "unlock_1",
		'info': '점프력이 상승합니다.',
		'level_info': '(한번만 익히는 스킬입니다.)',
		'nope_skill': ["none"],
		'need_level': 5,
	},
	'Crazing Air Knife': {
		'skillname': "skill5",
		'need_skillp': 2,
		'max': 5,
		'skillbook': -1,
		'info': '공중에서의 칼 데미지가 상승합니다..',
		'level_info': '익힐때마다 효과가 10％ 상승합니다.',
		'nope_skill': ["none"],
		'need_level': 10,
	},
}

STET_LIST_PRINT = (
"체력",
"근력",
"민첩",
"MP",
)

BUYMENU_LIST_PRINT = (
"Armor + 4",
"Armor + 20",
"Remote Human",
"Be Doctor",
"Unlimited Ammo",
"C4",
"Flashbang",
"Be Nurse",
"Human : Be Sniper",
"Human : Be Juggernut",
"Human : Be Shotgunner",
"Weapon World",
"HE Grenade World",
"Web Share",
"Rich or Poor",
"Be : Soldier(AR)",
"Be : Soldier(SR)",
)

BUYMENU_LIST = {
	'Be Nurse': {
		'skill': "None",
		'skill_max': 0,
		'need_unlock': "None",
		'dollar': 5000,
		'mp': 15,
		'need_level': 20,
	},
	'Flashbang': {
		'skill': "None",
		'skill_max': 0,
		'need_unlock': "None",
		'dollar': 2000,
		'mp': 9,
		'need_level': 20,
	},
	'Be : Soldier(SR)': {
		'skill': "None",
		'skill_max': 0,
		'need_unlock': "unlock_4",
		'dollar': 1,
		'mp': 0,
		'need_level': 1,
	},
	'Be : Soldier(AR)': {
		'skill': "None",
		'skill_max': 0,
		'need_unlock': "unlock_3",
		'dollar': 1,
		'mp': 0,
		'need_level': 1,
	},
	'Armor + 4': {
		'skill': "None",
		'skill_max': 0,
		'need_unlock': "None",
		'dollar': 500,
		'mp': 0,
		'need_level': -1,
	},
	'Armor + 20': {
		'skill': "None",
		'skill_max': 0,
		'need_unlock': "None",
		'dollar': 2500,
		'mp': 0,
		'need_level': -1,
	},
	'Rich or Poor': {
		'skill': "None",
		'skill_max': 0,
		'need_unlock': "None",
		'dollar': 5000,
		'mp': 0,
		'need_level': 1,
	},
	'Web Share': {
		'skill': "None",
		'skill_max': 0,
		'need_unlock': "None",
		'dollar': 5000,
		'mp': 0,
		'need_level': 1,
	},
	'Remote Human': {
		'skill': "None",
		'skill_max': 0,
		'need_unlock': "None",
		'dollar': 5000,
		'mp': 0,
		'need_level': 1,
	},
	'Be Doctor': {
		'skill': "None",
		'skill_max': 0,
		'need_unlock': "None",
		'dollar': 2000,
		'mp': 1,
		'need_level': 1,
	},
	'Unlimited Ammo': {
		'skill': "None",
		'skill_max': 0,
		'need_unlock': "None",
		'dollar': 10000,
		'mp': 0,
		'need_level': 1,
	},
	'C4': {
		'skill': "None",
		'skill_max': 0,
		'need_unlock': "None",
		'dollar': 1800,
		'mp': 1,
		'need_level': 1,
	},
	'Human : Be Sniper': {
		'skill': "None",
		'skill_max': 0,
		'need_unlock': "None",
		'dollar': 6000,
		'mp': 5,
		'need_level': 30,
	},
	'Human : Be Shotgunner': {
		'skill': "None",
		'skill_max': 0,
		'need_unlock': "None",
		'dollar': 6000,
		'mp': 5,
		'need_level': 30,
	},
	'Human : Be Juggernut': {
		'skill': "None",
		'skill_max': 0,
		'need_unlock': "None",
		'dollar': 5000,
		'mp': 5,
		'need_level': 30,
	},
	'Weapon World': {
		'skill': "None",
		'skill_max': 0,
		'need_unlock': "None",
		'dollar': 5000,
		'mp': 0,
		'need_level': 30,
	},
	'HE Grenade World': {
		'skill': "None",
		'skill_max': 0,
		'need_unlock': "None",
		'dollar': 10000,
		'mp': 10,
		'need_level': 35,
	},
}

IN_ATTACK = (1 << 0)
IN_JUMP = (1 << 1)
IN_DUCK = (1 << 2)
IN_FORWARD = (1 << 3)
IN_BACK = (1 << 4)
IN_USE = (1 << 5)
IN_CANCEL = (1 << 6)
IN_LEFT = (1 << 7)
IN_RIGHT = (1 << 8)
IN_MOVELEFT = (1 << 9)
IN_MOVERIGHT = (1 << 10)
IN_ATTACK2 = (1 << 11)
IN_RUN = (1 << 12)
IN_RELOAD = (1 << 13)
IN_ALT1 = (1 << 14)
IN_ALT2 = (1 << 15)
IN_SCORE = (1 << 16)   # Used by client.dll for when scoreboard is held down
IN_SPEED = (1 << 17) # Player is holding the speed key
IN_WALK = (1 << 18) # Player holding walk key
IN_ZOOM = (1 << 19 )# Zoom key for HUD zoom
IN_WEAPON1 = (1 << 20) # weapon defines these bits
IN_WEAPON2 = (1 << 21) # weapon defines these bits
IN_BULLRUSH = (1 << 22)
IN_GRENADE1 = (1 << 23) # grenade 1
IN_GRENADE2 = (1 << 24) # grenade 2
IN_ATTACK3 = (1 << 25)

def kaboom_gamble1(userid2):
	index = es.getentityindex("npc_ticket_nightfever")
	es.emitsound('entity', index, 'ambient/explosions/explode_%s.wav' % random.randint(1, 8), 1.0, 0.85)
	es.remove("npc_ticket_nightfever")
	npc_location = (-961, 439, 32)
	userid = es.getuserid()
	es.server.cmd('es_xgive %s env_explosion' %(userid))
	last_give = int(sv('eventscripts_lastgive'))
	es.entitysetvalue(last_give, "classname", "team_explosion")
	wide = 10000
	damage = 10000
	es.server.cmd('es_xfire %s team_explosion addoutput "imagnitude %s\"' % (userid, wide))
	es.server.cmd('es_xfire %s team_explosion addoutput "iradiusoverride %s\"' % (userid, damage))
	es.setindexprop(last_give, 'CBaseEntity.m_hOwnerEntity', 0)
	est.entteleport(last_give, npc_location[0], npc_location[1], npc_location[2])
	es.server.cmd('es_xfire %s team_explosion explode' % userid)
	username = es.getplayername(userid2)
	npc_msg("#255,125,0???", "이 자식들! 내 도박 머신을 망가뜨리다니!!")
	gamethread.delayed(4, npc_msg, ("#255,255,255%s" %(username), "너는 도박의 신 #255,125,0하까나이#default... 내가 분명 경찰에 철컹철컹 해놨을텐데..!")) 
	gamethread.delayed(8, npc_msg, ("#255,125,0하까나이", "더 이상 말은 필요 없다! 덤벼라!"))
	bgm_loop.stop()
	est.play("#h", "zeisenproject_-1/autosounds/story_sounds/znm.mp3")
	est.stopsound("#h", "zeisenproject_-1/de_nightfever/%s.mp3" %(sv('today')))
	gamethread.delayed(8, es.server.cmd, ('bot_add_ct "[Gunner] 하까나이"'))
	es.server.cmd('es_xdelayed 8 bot_add_ct "[Gunner] 하까나이"')

def gamble_select1(userid, choice, popupname):
	if int(sv('say_block')) == 0 and es.getentityindex("npc_ticket_nightfever") > 0 and es.getplayerteam(userid) > 1:
		index = es.getentityindex("npc_ticket_nightfever")
		login_id = getplayerid(userid)
		money = int(es.keygetvalue(login_id, "player_data", "money"))
		victim_location = vecmath.vector(es.getplayerlocation(userid))
		attacker_location = vecmath.vector(es.getindexprop(index, "CBaseEntity.m_vecOrigin").split(","))
		distance = vecmath.distance(victim_location, attacker_location) * 0.0254
		if distance > 3: money = 0
		if money >= int(choice):
			es.set("say_block", 1)
			the_delay = 13
			keymath(login_id, "player_data", "money", "-", choice)
			username = es.getplayername(userid)
			first_card = random.choice(["7", "바나나", "바나나", "포도", "포도", "포도", "사과", "사과", "사과", "사과"])
			second_card = random.choice(["7", "바나나", "바나나", "포도", "포도", "포도", "사과", "사과", "사과", "사과"])
			third_card = random.choice(["7", "바나나", "바나나", "포도", "포도", "포도", "사과", "사과", "사과", "사과"])
			if str(first_card) == "7": themuch = 777
			if str(first_card) == "바나나": themuch = 8
			if str(first_card) == "포도": themuch = 6
			if str(first_card) == "사과": themuch = 2
			for theuserid in es.getUseridList():
				gamethread.delayed(0.01, usermsg.centermsg, (theuserid, "%s님의 777 도박을 시도합니다(%s엔)" %(username, choice)))
				gamethread.delayed(0.01, es.playsound, (theuserid, "buttons/combine_button_locked.wav", 1.0))
				gamethread.delayed(3, usermsg.centermsg, (theuserid, "%s님의 777 도박(%s엔)\n \n%s" %(username, choice, first_card)))
				gamethread.delayed(4, usermsg.centermsg, (theuserid, "%s님의 777 도박(%s엔)\n \n%s" %(username, choice, first_card)))
				gamethread.delayed(5, usermsg.centermsg, (theuserid, "%s님의 777 도박(%s엔)\n \n%s" %(username, choice, first_card)))
				gamethread.delayed(3, es.playsound, (theuserid, "buttons/button9.wav", 1.0))
				gamethread.delayed(6, usermsg.centermsg, (theuserid, "%s님의 777 도박(%s엔)\n \n%s\n%s" %(username, choice, first_card, second_card)))
				gamethread.delayed(7, usermsg.centermsg, (theuserid, "%s님의 777 도박(%s엔)\n \n%s\n%s" %(username, choice, first_card, second_card)))
				gamethread.delayed(8, usermsg.centermsg, (theuserid, "%s님의 777 도박(%s엔)\n \n%s\n%s" %(username, choice, first_card, second_card)))
				gamethread.delayed(6, es.playsound, (theuserid, "buttons/button9.wav", 1.0))
				gamethread.delayed(9, usermsg.centermsg, (theuserid, "%s님의 777 도박(%s엔)\n \n%s\n%s\n%s" %(username, choice, first_card, second_card, third_card)))
				gamethread.delayed(9, es.playsound, (theuserid, "buttons/button9.wav", 1.0))
				if str(first_card) == str(second_card) and str(first_card) == str(third_card):
					gamethread.delayed(11, usermsg.centermsg, (theuserid, "%s님이 %s 엔을 획득했습니다!" %(username, int(choice) * themuch)))
					gamethread.delayed(11, es.playsound, (theuserid, "buttons/button5.wav", 1.0))
				else:
					gamethread.delayed(11, es.playsound, (theuserid, "buttons/button8.wav", 1.0))
			if str(first_card) == str(second_card) and str(first_card) == str(third_card):
				gamethread.delayed(11, keymath, (login_id, "player_data", "money", "+", int(choice) * themuch))
			else:
				if random.randint(4,44) == 4:
					gamethread.delayed(11, kaboom_gamble1, (userid))
					the_delay = 25
			gamethread.delayed(the_delay, es.set, ("say_block", 0))
def load():
	exist_setv("zombie_count", 0)
	exist_setv("server_time", 0)
	if str(sv('server_time')) == "0":
		server_time = time.strftime('%H시 %M분 %S초 (대한민국 표준시)')
		es.set("server_time", server_time)
	exist_setv("level", 1)
	exist_setv("load_check", 0)
	exist_setv("n_route", "")
	exist_setv("player_count", 0)
	exist_setv("black_fade", 0)
	exist_setv("say_block", 0)
	exist_setv("allfade", 0)
	exist_setv("fight", 0)
	exist_setv("server_update", 0)
	es.set("attack_will", 0)
	load_check = svmath("load_check", "+", 1)
	es.server.cmd('eventscripts_noisy 1')
	global timerz
	timerz = repeat.create('timerz', timerz_command, ())
	timerz.start(1, 99999999)
	global timerx
	timerx = repeat.create('timerx', timerx_command, ())
	timerx.start(30, 99999999)
	cmdlib.registerServerCommand('r_hudchat', hudchat, 'eee')
	cmdlib.registerServerCommand('r_makechat', makechat, 'eee')
	cmdlib.registerServerCommand('r_givesupport', gsupport, 'eee')
	spe.parseTypesINI("bot/twosig.ini")
	spe.parseINI("bot/sig.ini")
	#spe.detourFunction("Follow", spe.HookType.Pre, PrePrintTest)
	spe.detourFunction("PlayerRunCommand", spe.HookType.Pre, PrePlayerRunCommand)
	#---------------------------------------------------------------------------------------------------------
	#Global Variable

	global lasermodel_1
	if "_" in themap(): lasermodel_1 = es.precachemodel("effects/gunshiptracer.vmt")

	global lasermodel_2
	if "_" in themap(): lasermodel_2 = es.precachemodel("effects/laser1.vmt")

	global bgm_loop
	bgm_loop = repeat.create('bgm_loop', bgm_loop, ())

	global z_max
	z_max = {}

	global max_health
	max_health = {}

	global id
	id = {}

	global one_damage_armor
	one_damage_armor = {}

	global one_damage
	one_damage = {}

	global sayok
	sayok = {}

	global current_mp
	current_mp = {}

	global top_damage
	top_damage = {}

	global burn_time
	burn_time = {}

	global respawn_time
	respawn_time = {}

	global IRON_MAN
	IRON_MAN = {}

	global IRON_MAN_PRESS_1
	IRON_MAN_PRESS_1 = {}

	global IRON_MAN_PRESS_2
	IRON_MAN_PRESS_2 = {}

	global unlock_p
	unlock_p = popuplib.easymenu('unlock_p', None, print_select)
	unlock_p.settitle("＠ Unlock List")
	for a in UNLOCK_LIST:
		unlock_p.addoption((UNLOCK_LIST[a]['unlock_info'], UNLOCK_LIST[a]['unlock']), a)

	global custom_p
	custom_p = popuplib.easymenu('custom_p', None, custom_p_select)
	custom_p.settitle("＠ Customize Skin")
	custom_p.addoption(("player/lockcha/lockcha11/glados.mdl"), "글라도스 미쿠")
	custom_p.addoption(("player/reisen/cirno/cirno"), "치르노")
	custom_p.addoption(("player/elis/fsv2/fischer.mdl"), "샘 피셔")
	custom_p.addoption(("player/hhp227/miku/miku"), "하츠네 미쿠")
	custom_p.addoption(("player/konata/zatsunemiku/zatsunemiku"), "자츠네 미쿠")
	custom_p.addoption(("player/konata/idol/idol"), "이로하")
	custom_p.addoption(("models/player/techknow/paranoya/paranoya.mdl"), "파라노야")
	custom_p.addoption(("models/player/knifelemon/tenko"), "텐시")
	custom_p.addoption(("player/slow/fallout_3/tesla_power_armor/slow.mdl"), "테슬라 파워 아머")

	global world_start
	world_start = popuplib.easymenu('world_start', None, world_select)
	world_start.settitle("＠ World Tour")
	world_start.addoption(("item3", "cs_complex"), "몬스터 월드")
	world_start.addoption(("item2", "de_colors"), "화이트 버드 페스티벌")
	world_start.addoption(("item7", "de_dust2_mariostyle"), "페어리 월드")
	world_start.addoption("A", "아이스 월드", 0)
	world_start.addoption("A", "??? 월드", 0)
	world_start.addoption("A", "다크 월드", 0)

	global inventor_shop_1
	inventor_shop_1 = popuplib.easymenu('inventor_shop_1', None, inventor_select)
	inventor_shop_1.settitle("＠ Inventor")
	inventor_shop_1.addoption((50000, "item5"), "50000엔 │ 파란색 물약")
	inventor_shop_1.addoption((65000, "item6"), "65000엔 │ 보라색 물약")

	global vampire_select_
	vampire_select_ = popuplib.create('vampire_select_1')
	vampire_select_.addline("＠ ???")
	vampire_select_.addline(" ")
	vampire_select_.addline("누군지 모르겠다..")
	vampire_select_.addline("어둠으로 가려져있고, 날개를 가지고 있다.")
	vampire_select_.addline("주점에서 보던 사람들과 다르게 우아한 옷을 입고있는것처럼 보인다.")
	vampire_select_.addline(" ")
	vampire_select_.addline("“ 어때요.. 저랑 놀지 않으실래요? ”")
	vampire_select_.addline(" ")
	vampire_select_.addline("->1. 좋아.")
	vampire_select_.addline("->2. 아니.")
	vampire_select_.addline(" ")
	vampire_select_.menuselect = vampire_select

	global vampire_select_2
	vampire_select_2 = popuplib.create('vampire_select_2')
	vampire_select_2.addline("＠ ???")
	vampire_select_2.addline(" ")
	vampire_select_2.addline("누군지 모르겠다..")
	vampire_select_2.addline("어둠으로 가려져있고, 날개를 가지고 있다.")
	vampire_select_2.addline("주점에서 보던 사람들과 다르게 우아한 옷을 입고있는것처럼 보인다.")
	vampire_select_2.addline("나를 이상한 표정으로 보고있다..")
	vampire_select_2.addline(" ")
	vampire_select_2.addline("“ 잘 생각해 보세요… 저랑 놀지 않으실래요?”")
	vampire_select_2.addline(" ")
	vampire_select_2.addline("->1. 좋아.")
	vampire_select_2.addline("->2. 아니.")
	vampire_select_2.addline(" ")
	vampire_select_2.menuselect = vampire_select

	global gamble_start
	gamble_start = popuplib.easymenu('gamble_start', None, gamble_select1)
	gamble_start.settitle("＠ 7 7 7")
	gamble_start.displaymode = "sticky"
	gamble_start.addoption(0, "777 777배, 바나나 8배, 포도 6배, 사과 2배", 0)
	gamble_start.addoption(200, "200엔을 베팅하고 시작한다.")
	gamble_start.addoption(400, "400엔을 베팅하고 시작한다.")
	gamble_start.addoption(1000, "1000엔을 베팅하고 시작한다.")
	gamble_start.addoption(2000, "2000엔을 베팅하고 시작한다.")
	gamble_start.addoption(4000, "4000엔을 베팅하고 시작한다.")
	gamble_start.addoption(7777, "7777엔을 베팅하고 시작한다.")
	gamble_start.addoption(8000, "8000엔을 베팅하고 시작한다.")
	gamble_start.addoption(10000, "10000엔을 베팅하고 시작한다.")
	global rpgmenu
	rpgmenu = popuplib.easymenu('rpgmenu', None, rpgmenu_select)
	rpgmenu.settitle("＠ Main Menu")
	rpgmenu.addoption("스킬", "스킬 (개발중)")
	rpgmenu.addoption("스텟", "스텟 (개발중)")
	rpgmenu.addoption("인벤토리", "인벤토리 (개발중)")
	top_damage['damage'] = 0
	top_damage['userid'] = 0
	for userid in getbot():
		respawn_time[userid] = 0
	for userid in gethuman():
		one_damage_armor[userid] = 0
		one_damage[userid] = 0
		sayok[userid] = 1
		z_max[userid] = 0
		current_mp[userid] = 0
	for f_userid in es.getUseridList():
		burn_time[f_userid] = 0
		IRON_MAN[f_userid] = 2
		IRON_MAN_PRESS_1[f_userid] = 0
		IRON_MAN_PRESS_2[f_userid] = 0
		current_mp[f_userid] = 0
		current_mp[f_userid] = int(sv('mp_%s' %(f_userid)))
		max_health[f_userid] = 0
		max_health[f_userid] = int(sv('max_health_%s' %(f_userid)))
	#---------------------------------------------------------------------------------------------------------
	spe.registerPreHook('player_hurt', pre_player_hurt)
	es.addons.registerClientCommandFilter(Commander4)
	es.addons.registerSayFilter(sayFilter)
	#es.addons.registerTickListener(ticklistener)
	cmdlib.registerServerCommand('r_unlock', unlock, 'eee')
	cmdlib.registerServerCommand('r_weaponswap', weaponswap, 'eee')

	check = es.exists("keygroup", "server_unlock")
	if check == 0:
		es.keygroupload("server_unlock", "|bot/server_data")
	else:
		es.keygroupsave("server_unlock", "|bot/server_data")
		es.keygroupdelete("server_unlock")
		es.keygroupload("server_unlock", "|bot/server_data")


	check = es.exists("keygroup", "total_players")
	if check == 0:
		es.keygroupload("total_players", "|bot/server_data")
	else:
		es.keygroupsave("total_players", "|bot/server_data")
		es.keygroupdelete("total_players")
		es.keygroupload("total_players", "|bot/server_data")

	check = es.exists("keygroup", "ranking_level")
	if check == 0:
		es.keygroupload("ranking_level", "|bot/server_data")
	else:
		es.keygroupsave("ranking_level", "|bot/server_data")
		es.keygroupdelete("ranking_level")
		es.keygroupload("ranking_level", "|bot/server_data")

	check = es.exists("keygroup", "ranking_m")
	if check == 0:
		es.keygroupload("ranking_m", "|bot/server_data")
	else:
		es.keygroupsave("ranking_m", "|bot/server_data")
		es.keygroupdelete("ranking_m")
		es.keygroupload("ranking_m", "|bot/server_data")

	check = es.exists("keygroup", "ranking_s")
	if check == 0:
		es.keygroupload("ranking_s", "|bot/server_data")
	else:
		es.keygroupsave("ranking_s", "|bot/server_data")
		es.keygroupdelete("ranking_s")
		es.keygroupload("ranking_s", "|bot/server_data")

	check = es.exists("keygroup", "ranking_p")
	if check == 0:
		es.keygroupload("ranking_p", "|bot/server_data")
	else:
		es.keygroupsave("ranking_p", "|bot/server_data")
		es.keygroupdelete("ranking_p")
		es.keygroupload("ranking_p", "|bot/server_data")
	rank_p_setting()
	rank_support_setting()
	rank_money_setting()
	rank_level_setting()
	es.set("teleport_timer", -1)
	global teleport_timer
	teleport_timer = repeat.create('teleport_timer', pass_command, ())
	es.regcmd('es_xgetuserid', 'bot/blocking')

def pass_command():
	pass

def gsupport(args):
	steamid = getplayerid(args[0])
	keymath(steamid, "player_data", "supporter_time", "+", (60*60*30))

def custom_p_select(userid, choice, popupname):
	login_id = getplayerid(userid)
	if str(login_id) in str(sv('support_ranker')):
		es.keysetvalue(login_id, "player_data", "fire_count", choice)
		npc_tell(userid, "#255,255,255레아", "자! 거울 한번 볼래?")
		est.setmodel(userid, choice)
	else: npc_tell(userid, "#255,255,255레아", "미안한데, 서포터 1-5위까지만 받아!")

def inventor_select(userid, choice, popupname):
	login_id = getplayerid(userid)
	buy_money = int(choice[0])
	buy_item = str(choice[1])
	money = int(es.keygetvalue(login_id, "player_data", "money"))
	if money >= buy_money:
		keymath(login_id, "player_data", buy_item, "+", 1)
		keymath(login_id, "player_data", "money", "-", buy_money)
		npc_tell(userid, "#255,255,255렉스", "내 발명품에 관심을 보여줘서 정말로 고맙네. 개발에 도움을 주는거야 이런건.")
		
def world_select(userid, choice, popupname):
	login_id = getplayerid(userid)
	item = int(es.keygetvalue(login_id, "player_data", choice[0]))
	if item > 0:
		if int(sv('bot_quota')) == 2 and int(sv('say_block')) == 0:
			if not israining():
				keymath(login_id, "player_data", choice[0], "-", 1)
				will_map = choice[1]
				bgm_loop.stop()
				nightfever_close3()
				x = 2022
				y = 1054
				z = 202
				for to_userid in es.getUseridList():
					if es.getplayerteam(to_userid) == 2:
						est.spawn(to_userid)
						gamethread.delayed(0.2, es.setpos, (to_userid, x, y, z))
						gamethread.delayed(0.2, es.setplayerprop, (to_userid, _blockprop, 2))
				npc_msg("#255,255,255베닉스", "조심하세요, 출발합니다.")
				esc.msg("#255,255,255다른 월드로 이동을 시작합니다. 약 3분 30초 걸립니다.")
				esc.msg("#255,255,255간혹 보스가 나타나 당신들의 이동을 방해할수도 있습니다. 주의하세요.")
				esc.msg("#255,255,255죽으면 당신은 서버에서 강제로 퇴장됩니다. 자신 스스로 방어하세요.")
				est.stopsound("#h", sv('mmusic'))
				est.play("#h", "zeisenproject_-1/autosounds/story_sounds/sound_22.mp3")
				random_bot = random.randint(1,4)
				if random_bot == 2:
					gkgk = repeat.create('gkgk', world_bot_1, ())
					gkgk.start(random.randint(30,50), 1)
				if random_bot == 3:
					gkgk = repeat.create('gkgk', world_bot_2, ())
					gkgk.start(random.randint(30,50), 1)
				es.set("will_map", will_map)
				es.set("teleport_timer", (180+33))

def world_bot_1():
	if themap() == "de_nightfever":
		if str(sv('sv_password')) == "nipperkk":
			world_begin()
			es.server.cmd('bot_add_ct "[Gunner] Elite Hunter"')
			es.server.cmd('bot_add_ct "[Shooter] 1"')
			es.server.cmd('bot_add_ct "[Shooter] 2"')
			es.server.cmd('bot_add_ct "[Shooter] 3"')
			es.server.cmd('bot_add_ct "[Shooter] 4"')
			es.server.cmd('bot_add_ct "[Shooter] 5"')
			es.server.cmd('bot_add_ct "[Shooter] 6"')
			es.server.cmd('bot_add_ct "[Shooter] 7"')
			es.server.cmd('bot_add_ct "[Shooter] 8"')
			es.server.cmd('bot_add_ct "[Shooter] 9"')
			es.server.cmd('bot_add_ct "[Shooter] 10"')
			es.server.cmd('bot_add_ct "[Shooter] 11"')
			es.server.cmd('bot_add_ct "[Shooter] 12"')
			es.server.cmd('bot_add_ct "[Shooter] 13"')
			es.server.cmd('bot_add_ct "[Shooter] 14"')
			es.server.cmd('bot_add_ct "[Shooter] 15"')
			es.server.cmd('bot_add_ct "[Shooter] 16"')
			es.set("zombie_count", 9999) 

def world_begin():
	est.stopsound("#h", "zeisenproject_-1/autosounds/story_sounds/sound_22.mp3")
	est.play("#h", "zeisenproject_-1/autosounds/story_sounds/sound_25.mp3")

def world_bot_2():
	if themap() == "de_nightfever":
		if str(sv('sv_password')) == "nipperkk":
			world_begin()
			es.server.cmd('bot_add_ct "[Gunner] Elite Sniper"')
			es.server.cmd('bot_add_ct "[Shooter] 1"')
			es.server.cmd('bot_add_ct "[Shooter] 2"')
			es.server.cmd('bot_add_ct "[Shooter] 3"')
			es.server.cmd('bot_add_ct "[Shooter] 4"')
			es.server.cmd('bot_add_ct "[Shooter] 5"')
			es.server.cmd('bot_add_ct "[Shooter] 6"')
			es.server.cmd('bot_add_ct "[Shooter] 7"')
			es.server.cmd('bot_add_ct "[Shooter] 8"')
			es.server.cmd('bot_add_ct "[Shooter] 9"')
			es.server.cmd('bot_add_ct "[Shooter] 10"')
			es.server.cmd('bot_add_ct "[Shooter] 11"')
			es.server.cmd('bot_add_ct "[Shooter] 12"')
			es.server.cmd('bot_add_ct "[Shooter] 13"')
			es.set("zombie_count", 9999) 


def rank_p_add(userid):
	login_id = getplayerid(userid)
	username = es.getplayername(userid)
	kv = keyvalues.getKeyGroup("ranking_p")
	for rank_id in kv:
		if login_id == rank_id: es.keydelete("ranking_p", rank_id)
	es.keycreate("ranking_p", login_id)
	es.keysetvalue("ranking_p", login_id, "username", "%s " %(username))
	es.keysetvalue("ranking_p", login_id, "level", es.keygetvalue(login_id, "player_data", "play_time"))
	es.keysetvalue("ranking_p", login_id, "mastery", es.keygetvalue(login_id, "player_data", "mastery"))
	es.keysetvalue("ranking_p", login_id, "clantag", "%s " %(getclantag(userid)))
	es.ServerCommand('keygroupsort ranking_p level des #numeric')

def rank_p_setting():
	es.ServerCommand('keygroupsort ranking_p level des #numeric')
	kv = keyvalues.getKeyGroup("ranking_p")
	rank_count = 1
	global ranking_p_popup
	ranking_p_popup = popuplib.easymenu('ranking_p_popup', None, none_select)
	ranking_p_popup.settitle("＠ 플레이 시간 랭킹")
	ranking_p_popup.c_stateformat[False] = "%2"
	ranking_p_popup.c_stateformat[True] = "%2"
	for steamid in kv:
		if rank_count > 25:
			es.keydelete("ranking_p", steamid)
			continue
		level = es.keygetvalue("ranking_p", steamid, "level")
		clantag = es.keygetvalue("ranking_p", steamid, "clantag")
		username = es.keygetvalue("ranking_p", steamid, "username")
		ranking_p_popup.addoption(steamid, "%s위. %s│ %sClan" %(rank_count, username, clantag))
		rank_count += 1
	es.keygroupsave("ranking_p", "|bot/server_data")

def rank_support_add(userid):
	login_id = getplayerid(userid)
	username = es.getplayername(userid)
	kv = keyvalues.getKeyGroup("ranking_s")
	for rank_id in kv:
		if login_id == rank_id: es.keydelete("ranking_s", rank_id)
	es.keycreate("ranking_s", login_id)
	es.keysetvalue("ranking_s", login_id, "username", "%s " %(username))
	es.keysetvalue("ranking_s", login_id, "level", es.keygetvalue(login_id, "player_data", "supporter_time"))
	es.keysetvalue("ranking_s", login_id, "mastery", es.keygetvalue(login_id, "player_data", "mastery"))
	es.keysetvalue("ranking_s", login_id, "clantag", "%s " %(getclantag(userid)))
	es.ServerCommand('keygroupsort ranking_s level des #numeric')

def rank_support_setting():
	es.ServerCommand('keygroupsort ranking_s level des #numeric')
	kv = keyvalues.getKeyGroup("ranking_s")
	rank_count = 1
	global ranking_s_popup
	ranking_s_popup = popuplib.easymenu('ranking_s_popup', None, none_select)
	ranking_s_popup.settitle("＠ 엔 랭킹")
	ranking_s_popup.c_stateformat[False] = "%2"
	ranking_s_popup.c_stateformat[True] = "%2"
	es.set("support_ranker", "")
	for steamid in kv:
		if rank_count == 1:
			es.set("support_ranker_1", steamid)
		if rank_count <= 5:
			ggg = "%s %s" %(sv('support_ranker'), steamid)
			es.set("support_ranker", ggg)
		if rank_count > 25:
			es.keydelete("ranking_s", steamid)
			continue
		level = es.keygetvalue("ranking_s", steamid, "level")
		spt = int(level)
		spt_min = spt / 60
		spt_min = est.rounddecimal(spt_min, 0)
		spt_min = spt_min.replace(".0", "")
		spt_sec = spt % 60
		spt_hour = int(spt_min) / 60
		spt_hour = est.rounddecimal(spt_hour, 0)
		spt_hour = spt_hour.replace(".0", "")
		if int(spt_hour) != 0:
			spt_min = int(spt_min) - (int(spt_hour) * 60)
		spt_day = int(spt_hour) / 24
		spt_day = est.rounddecimal(spt_day, 0)
		spt_day = spt_day.replace(".0", "")
		if int(spt_day) != 0:
			spt_hour = int(spt_hour) - (int(spt_day) * 24)
		mg = "%s일 %s시 %s분 %s초" %(spt_day, spt_hour, spt_min, spt_sec)
		mg_args = mg.split()
		if mg_args[0] == "0일": mg = mg.replace("0일 ", "")
		if mg_args[1] == "0시": mg = mg.replace("0시 ", "")
		if mg_args[2] == "0분": mg = mg.replace("0분 ", "")
		if mg_args[3] == "0초": mg = mg.replace(" 0초", "")
		clantag = es.keygetvalue("ranking_s", steamid, "clantag")
		username = es.keygetvalue("ranking_s", steamid, "username")
		ranking_s_popup.addoption(steamid, "%s위. %s [Time : %s] │ %sClan" %(rank_count, username, mg, clantag))
		rank_count += 1
	es.keygroupsave("ranking_s", "|bot/server_data")

def rank_money_add(userid):
	login_id = getplayerid(userid)
	username = es.getplayername(userid)
	kv = keyvalues.getKeyGroup("ranking_m")
	for rank_id in kv:
		if login_id == rank_id: es.keydelete("ranking_m", rank_id)
	es.keycreate("ranking_m", login_id)
	es.keysetvalue("ranking_m", login_id, "username", "%s " %(username))
	es.keysetvalue("ranking_m", login_id, "level", es.keygetvalue(login_id, "player_data", "money"))
	es.keysetvalue("ranking_m", login_id, "mastery", es.keygetvalue(login_id, "player_data", "mastery"))
	es.keysetvalue("ranking_m", login_id, "clantag", "%s " %(getclantag(userid)))
	es.ServerCommand('keygroupsort ranking_m level des #numeric')

def rank_money_setting():
	es.ServerCommand('keygroupsort ranking_m level des #numeric')
	kv = keyvalues.getKeyGroup("ranking_m")
	rank_count = 1
	global ranking_m_popup
	ranking_m_popup = popuplib.easymenu('ranking_m_popup', None, none_select)
	ranking_m_popup.settitle("＠ 엔 랭킹")
	ranking_m_popup.c_stateformat[False] = "%2"
	ranking_m_popup.c_stateformat[True] = "%2"
	for steamid in kv:
		if rank_count > 25:
			es.keydelete("ranking_m", steamid)
			continue
		level = es.keygetvalue("ranking_m", steamid, "level")
		clantag = es.keygetvalue("ranking_m", steamid, "clantag")
		username = es.keygetvalue("ranking_m", steamid, "username")
		ranking_m_popup.addoption(steamid, "%s위. %s%s엔 보유 │ %sClan" %(rank_count, username, level, clantag))
		rank_count += 1
	es.keygroupsave("ranking_m", "|bot/server_data")

def rank_level_add(userid):
	login_id = getplayerid(userid)
	username = es.getplayername(userid)
	kv = keyvalues.getKeyGroup("ranking_level")
	for rank_id in kv:
		if login_id == rank_id: es.keydelete("ranking_level", rank_id)
	es.keycreate("ranking_level", login_id)
	es.keysetvalue("ranking_level", login_id, "username", "%s " %(username))
	es.keysetvalue("ranking_level", login_id, "level", es.keygetvalue(login_id, "player_data", "level"))
	es.keysetvalue("ranking_level", login_id, "mastery", es.keygetvalue(login_id, "player_data", "mastery"))
	es.keysetvalue("ranking_level", login_id, "clantag", "%s " %(getclantag(userid)))

def rank_level_setting():
	es.ServerCommand('keygroupsort ranking_level level des #numeric')
	kv = keyvalues.getKeyGroup("ranking_level")
	rank_count = 1
	global ranking_level_popup
	ranking_level_popup = popuplib.easymenu('ranking_level_popup', None, none_select)
	ranking_level_popup.settitle("＠ 레벨 랭킹")
	ranking_level_popup.c_stateformat[False] = "%2"
	ranking_level_popup.c_stateformat[True] = "%2"
	for steamid in kv:
		if rank_count > 25:
			es.keydelete("ranking_level", steamid)
			continue
		level = es.keygetvalue("ranking_level", steamid, "level")
		clantag = es.keygetvalue("ranking_level", steamid, "clantag")
		username = es.keygetvalue("ranking_level", steamid, "username")
		ranking_level_popup.addoption(steamid, "%s위. %s[Lv. %s] │ %sClan" %(rank_count, username, level, clantag))
		rank_count += 1
	es.keygroupsave("ranking_level", "|bot/server_data")

def delete_server_data():
	kv = keyvalues.getKeyGroup("total_players")
	for steamid in kv:
		register_check = int(es.keygetvalue("total_players", steamid, "register"))
		if reigster_check == 0: es.keydelete("total_players", steamid)
		else:
			register_id = str(es.keygetvalue("total_players", steamid, "register_id"))
			if register_id == "0": es.keydelete("total_players", steamid)
	es.keygroupsave("total_players", "|bot/server_data")

def timerx_command():
	for userid in es.getUseridList():
		if not es.isbot(userid):
			steamid = getplayerid(userid)
			es.keygroupsave(steamid, "|bot/player_data")

def block_test():
	f = es.getuserid("STEAM_0:0:21059511")
	es.msg(f)

def blocking(userid = None):
	es.msg("es_xgetuserid spotted! blocking...")

def unload():
	popuplib.delete('unlock_p')
	popuplib.delete('rpgmenu')
	popuplib.delete('ranking_level_popup')
	popuplib.delete('ranking_m_popup')
	popuplib.delete('gamble_start')
	popuplib.delete('inventor_shop_1')
	popuplib.delete('vampire_select_1')
	popuplib.delete('vampire_select_2')
	repeat.delete('timerz')
	repeat.delete('timerx')
	repeat.delete('bgm_loop')
	#cmdlib.unregisterServerCommand('es_xuserid')
	cmdlib.unregisterServerCommand('r_hudchat')
	cmdlib.unregisterServerCommand('r_makechat')
	cmdlib.unregisterServerCommand('r_givesupport')
	spe.unregisterPreHook('player_hurt', pre_player_hurt)
	es.addons.unregisterClientCommandFilter(Commander4)
	#es.addons.unregisterTickListener(ticklistener)
	es.addons.unregisterSayFilter(sayFilter)
	#spe.undetourFunction("Follow", spe.HookType.Pre, PrePrintTest)
	spe.undetourFunction("PlayerRunCommand", spe.HookType.Pre, PrePlayerRunCommand)
	cmdlib.unregisterServerCommand('r_unlock')
	cmdlib.unregisterServerCommand('r_weaponswap')
	for a in es.getUseridList():
		if es.getplayerteam(a) > 1:
			if not es.isbot(a):
				es.set("mp_%s" %(a), current_mp[a])
	for a in es.getUseridList():
		if es.getplayerteam(a) > 1:
			es.set("max_health_%s" %(a), max_health[a])


def ticklistener():
	for index in es.getEntityIndexes("weapon_hegrenade"):
		if not int(es.getindexprop(index, "CHEGrenade.baseclass.m_bPinPulled")):
			if float(es.getindexprop(index, "CBaseCombatWeapon.LocalActiveWeaponData.m_flNextPrimaryAttack")) > 1:
				es.setindexprop(index, "CHEGrenade.baseclass.m_bRedraw", 0)

def PrePrintTest(args):
	target = get_userid_from_pointer(args[0])
	target2 = get_userid_from_pointer(args[1])
	es.msg("follow function(bot : %s, target : %s)" %(target2, target))
	return (spe.HookAction.Continue, 0)

def get_userid_from_pointer(ptr):
	for userid in es.getUseridList():
		if spe.getPlayer(userid) == ptr:
			return userid
	return None

def z_nearcoord_another(xx, yy, zz, x, y, z, allow_distance):
	victim_location = vecmath.vector(x, y, z)
	attacker_location = vecmath.vector(xx, yy, zz)
	distance = vecmath.distance(victim_location, attacker_location) * 0.0254
	if float(distance) <= float(allow_distance):
		return 1
	return 0

def PrePlayerRunCommand(args):
	return (spe.HookAction.Continue, 0)
	ucmd = spe.makeObject('CUserCmd', args[0])
	userid = get_userid_from_pointer(args[2])
	if userid:
		if est.isalive(userid):
			if not es.isbot(userid):
				login_id = getplayerid(userid)
				weapon = est.getgun(userid)
				weapon_index = est.getweaponindex(userid, weapon)
				if weapon == "weapon_knife":
					mastery = str(es.keygetvalue(login_id, "player_data", "mastery"))
					if mastery == "아이언 맨 ":
						if ucmd.buttons & IN_ATTACK:
							if IRON_MAN_PRESS_1[userid] == 0:
								IRON_MAN_PRESS_1[userid] = 1
								if IRON_MAN[userid] == 2:
									random_sound = random.randint(2,3)
									IRON_MAN[userid] = random_sound
									if random_sound == 2: usermsg.hudmsg(userid, "Press Left Mouse", 999, 0.3, 0.3)
									if random_sound == 3: usermsg.hudmsg(userid, "Press Right Mouse", 999, 0.3, 0.3)
									es.emitsound("player", userid, "zeisenproject_-1/autosounds/ironman_%s.wav" %(random_sound), 1.0, 1.0)
									es.setindexprop(weapon_index, "CBaseCombatWeapon.LocalActiveWeaponData.m_flNextPrimaryAttack", 0)
									es.setindexprop(weapon_index, "CBaseCombatWeapon.LocalActiveWeaponData.m_flNextSecondaryAttack", 0)
									es.setplayerprop(userid, "CCSPlayer.baseclass.baseclass.bcc_localdata.m_flNextAttack", 0)
								else: es.server.cmd('damage %s 100' %(userid))
						if not ucmd.buttons & IN_ATTACK:
							if IRON_MAN_PRESS_1[userid] == 1:
								IRON_MAN_PRESS_1[userid] = 0
						if ucmd.buttons & IN_ATTACK2:
							if IRON_MAN_PRESS_2[userid] == 0:
								IRON_MAN_PRESS_2[userid] = 1
								if IRON_MAN[userid] == 3:
									random_sound = random.randint(2,3)
									IRON_MAN[userid] = random_sound
									if random_sound == 2: usermsg.hudmsg(userid, "Press Left Mouse", 999, 0.3, 0.3)
									if random_sound == 3: usermsg.hudmsg(userid, "Press Right Mouse", 999, 0.3, 0.3)
									es.emitsound("player", userid, "zeisenproject_-1/autosounds/ironman_%s.wav" %(random_sound), 1.0, 1.0)
									es.setindexprop(weapon_index, "CBaseCombatWeapon.LocalActiveWeaponData.m_flNextPrimaryAttack", 0)
									es.setindexprop(weapon_index, "CBaseCombatWeapon.LocalActiveWeaponData.m_flNextSecondaryAttack", 0)
									es.setplayerprop(userid, "CCSPlayer.baseclass.baseclass.bcc_localdata.m_flNextAttack", 0)
								else: es.server.cmd('damage %s 100' %(userid))
						if not ucmd.buttons & IN_ATTACK2:
							if IRON_MAN_PRESS_2[userid] == 1:
								IRON_MAN_PRESS_2[userid] = 0
				r,g,b,a = getweaponcolor(weapon_index)
				if r == 0 and g == 255 and b == 0:
					es.setindexprop(weapon_index, "CWeaponCSBaseGun.baseclass.m_fAccuracyPenalty", 0.0)
					es.setindexprop(weapon_index, "CWeaponCSBaseGun.baseclass.m_weaponMode", 1)
					#es.setplayerprop(userid, "CBasePlayer.localdata.m_Local.m_vecPunchAngle", "0,0,0")
			#if es.getplayersteamid(userid) == "STEAM_0:0:21059511":
			#	target_format = getaimbot_target2(userid)
			#	if target_format[1]:
			#		x,y,z = getEyeLocation(target_format[1])
			#		viewCoord(userid, (x,y,z-3)) 
			#		if not ucmd.buttons & IN_ATTACK: ucmd.buttons += IN_ATTACK
			if es.isbot(userid):
				name = es.getplayername(userid)
				thegun = est.getgun(userid)
				#if float(es.getplayerprop(userid, "CCSPlayer.m_flFlashDuration")) > 0:
				#	if not ucmd.buttons & IN_ATTACK: ucmd.buttons += IN_ATTACK
				if ucmd.buttons & IN_SPEED: ucmd.buttons &= ~IN_SPEED
				if "[Human]" in name:
					if ucmd.forwardmove == 0 and ucmd.sidemove == 0:
						ucmd.buttons += IN_DUCK
				if not "[Human]" in name:
					if thegun == "weapon_knife":
						if onGround(userid) == 0:
							ucmd.forwardmove = 999
						if ucmd.forwardmove <= 0 and ucmd.sidemove == 0:
							if not ucmd.buttons & IN_DUCK:
								ucmd.forwardmove = 999
				if thegun == "weapon_knife":
					if random.randint(1,777) == 77:
						if not ucmd.buttons & IN_JUMP:
							ucmd.buttons += IN_JUMP
					else:
						if random.randint(1,100) == 1:
							if not ucmd.buttons & IN_DUCK:
								ucmd.buttons += IN_DUCK
				if name == "[Unknown] Crizi":
					if not ucmd.buttons & IN_ATTACK:
						ucmd.buttons += IN_ATTACK
				if name == "[Reckless] Fade":
					if est.getgun(userid) == "weapon_hegrenade":
						if ucmd.buttons & IN_ATTACK:
							if random.randint(1,5) == 1: ucmd.buttons -= IN_ATTACK
				if "[Bomber]" in name:
					if thegun in "weapon_hegrenade, weapon_flashbang":
						if ucmd.buttons & IN_ATTACK:
							if random.randint(1,2) == 2: ucmd.buttons &= ~IN_ATTACK
						if random.randint(1,2) == 2: ucmd.buttons += IN_ATTACK
					if ucmd.buttons & IN_JUMP:
						if random.randint(1,20) <= 19:
							ucmd.buttons &= ~IN_JUMP
	return (spe.HookAction.Continue, 0)

def getaimbot_target(zeisen_id):
	player_distance = []
	for userid in es.getUseridList():
		if es.getplayerteam(userid) == int(sv('humanteam')):
			if est.isalive(userid):
				x1,y1,z1 = es.getplayerlocation(userid)
				x2,y2,z2 = es.getplayerlocation(zeisen_id)
				distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5
				if not isWallBetween(zeisen_id, userid):
					player_distance.append((distance, userid))
	return min(player_distance) if player_distance else (None, None)

def getaimbot_target2(zeisen_id):
	player_distance = []
	for userid in es.getUseridList():
		if es.getplayerteam(userid) == int(sv('humanteam')):
			if est.isalive(userid):
				x1,y1,z1 = es.getplayerlocation(userid)
				x2,y2,z2 = es.getplayerlocation(zeisen_id)
				distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5
				player_distance.append((distance, userid))
	perfect = 1
	while perfect:
		if str(player_distance) != "[]":
			get_first = min(player_distance)
			if isWallBetween(zeisen_id, get_first[1]):
				player_distance.remove(get_first)
			else:
				perfect = 0
		else: perfect = 0	
	return min(player_distance) if player_distance else (None, None)

def print_select(userid, choice, popupname):
	esc.tell(userid, choice[0])
	steamid = getplayerid(userid)
	toto = "count_%s" %(choice[1])
	gogo = es.keygetvalue(steamid, "player_data", toto)
	if gogo:
		esc.tell(userid, "#0,255,255언락 카운트 : %s" %(gogo))

def hudchat(args):
	x = 0.25
	y = 0.25
	for userid in es.getUseridList():
		usermsg.hudmsg(sv('the_id'), args[0], random.randint(0,9999), float(random.randint(0,100)) / 100, float(random.randint(1,100)) / 100, r1=random.randint(0,255), g1=random.randint(0,255), b1=random.randint(0,255))

def makechat(args):
	esc.msg("%s :#default %s" %(args[0], args[1]))

def rpgmenu_select(userid, choice, popupname):
	steamid = es.getplayersteamid(userid)
	login_id = str(getplayerid(userid))
	if choice == "스킬":
		skillmenu = popuplib.easymenu('skill_%s' %(userid), None, skill_select)
		skillmenu.settitle("＠ 스킬 메뉴")
		skillmenu.c_endsep = " \n○ 원하는 스킬을 선택하세요\n "
		for a in SKILL_TEST_PRINT:
			skillbook = SKILL_TEST[a]['skillbook']
			if skillbook == -1:
				get_skill = int(es.keygetvalue(login_id, "player_data", SKILL_TEST[a]['skillname']))
				get_state = 1
				if int(es.keygetvalue(login_id, "player_data", "level")) < SKILL_TEST[a]['need_level']: get_state = 0
				if get_skill >= SKILL_TEST[a]['max']: get_state = 0
				if int(es.keygetvalue(login_id, "player_data", "skillpoint")) < SKILL_TEST[a]['need_skillp']: get_state = 0
				skillmenu.addoption(a, "%s (Lv.%s)[%s/%s] - %s SP" %(a, SKILL_TEST[a]['need_level'], get_skill, SKILL_TEST[a]['max'], SKILL_TEST[a]['need_skillp']), get_state)
			else:
				if not "unlock" in str(skillbook):
					item_name = ITEM_LIST[int(skillbook)]['name']
					skillbook_get = int(es.keygetvalue(login_id, "player_data", item_name))
					if skillbook_get > 0:
						get_skill = int(es.keygetvalue(login_id, "player_data", SKILL_TEST[a]['skillname']))
						get_state = 1
						if get_skill >= SKILL_TEST[a]['max']: get_state = 0
						if int(es.keygetvalue(login_id, "player_data", "skillpoint")) < SKILL_TEST[a]['need_skillp']: get_state = 0
						skillmenu.addoption(a, "%s [%s/%s] - %s SP" %(a, get_skill, SKILL_TEST[a]['max'], SKILL_TEST[a]['need_skillp']), get_state)
				if "unlock" in str(skillbook):
					item_name = str(skillbook)
					skillbook_get = int(es.keygetvalue(login_id, "player_data", item_name))
					if skillbook_get > 0:
						get_skill = int(es.keygetvalue(login_id, "player_data", SKILL_TEST[a]['skillname']))
						get_state = 1
						if get_skill >= SKILL_TEST[a]['max']: get_state = 0
						if int(es.keygetvalue(login_id, "player_data", "skillpoint")) < SKILL_TEST[a]['need_skillp']: get_state = 0
						skillmenu.addoption(a, "%s [%s/%s] - %s SP" %(a, get_skill, SKILL_TEST[a]['max'], SKILL_TEST[a]['need_skillp']), get_state)
		skillmenu.send(userid)
		popuplib.delete('skill_%s' %(userid))
	if choice == "스텟":
		skillmenu = popuplib.easymenu('skill_%s' %(userid), None, stet_select)
		skillmenu.settitle("＠ 스텟 메뉴")
		skillmenu.c_endsep = " \n○ 익힐때 마다 스텟 포인트는 1 감소됩니다.\n "
		for a in STET_LIST_PRINT:
			stetpoint = int(es.keygetvalue(login_id, "player_data", "stetpoint"))
			state = 1
			if stetpoint <= 0: state = 0
			if a == "체력": thename = "health"
			if a == "근력": thename = "power"
			if a == "민첩": thename = "speed"
			print_a = a
			if a == "MP": thename = "MP"
			if print_a == "MP": print_a = "MP "
			thevalue = es.keygetvalue(login_id, "player_data", thename)
			skillmenu.addoption(a, "%s │ %s" %(print_a, thevalue), state)
		skillmenu.send(userid)
		popuplib.delete('skill_%s' %(userid))
	if choice == "인벤토리":
		inventory = popuplib.easymenu('inventory_%s' %(userid), None, inventory_select)
		inventory.settitle("＠ 인벤토리 메뉴")
		for item_code in ITEM_LIST:
			name = ITEM_LIST[item_code]['name']
			item_count = int(es.keygetvalue(login_id, "player_data", name))
			if item_count >= 1:		
				showname = ITEM_LIST[item_code]['showname']
				inventory.addoption(item_code, "%s(%s) : %s" %(showname, item_code, item_count))
		inventory.send(userid)
		popuplib.delete('inventory_%s' %(userid))	

def inventory_select(userid, choice, popupname):
	steamid = es.getplayersteamid(userid)
	login_id = str(getplayerid(userid))
	inventory = popuplib.easymenu('inventory_%s' %(userid), None, inventory2_select)
	showname = ITEM_LIST[choice]['showname']
	inventory.settitle("＠ %s" %(showname))
	_info = ITEM_LIST[choice]['info']
	_effect_info = ITEM_LIST[choice]['effect_info']
	inventory.setdescription(" \n＊ %s\n○ %s" %(_info, _effect_info))
	state_1 = int(ITEM_LIST[choice]['allow_use'])
	inventory.addoption(choice, "이 아이템을 사용한다.", state_1)
	inventory.send(userid)
	popuplib.delete('inventory_%s' %(userid))
	
def inventory2_select(userid, choice, popupname):
	username = es.getplayername(userid)
	showname = ITEM_LIST[choice]['showname']
	steamid = getplayerid(userid)
	login_id = steamid
	item_used = 1
	if int(choice) == 2:
		if not themap() in str(NORMAL_WORLD):
			es.server.cmd('sm_votemap cs_assault2_goban_b3')
		else:
			item_used = 0
			esc.tell(userid, "#255,255,255이미 노말 월드에 있습니다.")
	if int(choice) == 3:
		item_used = 0
		esc.tell(userid, "#255,255,255아침에 나타나는 베닉스의 투어를 통해 이동할수 있습니다.")
	if int(choice) == 5:
		if random.randint(1,3) == 2:
			esc.msg("#0,255,255[Use]#255,255,255 %s : 온 몸이 편안해졌다." %(username))
			level = int(es.keygetvalue(login_id, "player_data", "level"))
			es.keysetvalue(login_id, "player_data", "stetpoint", level)
			es.keysetvalue(login_id, "player_data", "health", 100)
			es.keysetvalue(login_id, "player_data", "power", 100)
			es.keysetvalue(login_id, "player_data", "speed", 1000)
			es.keysetvalue(login_id, "player_data", "mp", 0)
		else:
			esc.msg("#0,255,255[Use]#255,255,255 %s : 피곤함이 몰려온다." %(username))
	if int(choice) == 6:
		if random.randint(1,3) == 2:
			esc.msg("#0,255,255[Use]#255,255,255 %s : 온 몸이 편안해졌다." %(username))
			level = int(es.keygetvalue(login_id, "player_data", "level"))
			es.keysetvalue(login_id, "player_data", "skillpoint", level)
			es.keysetvalue(login_id, "player_data", "skill1", 0)
			es.keysetvalue(login_id, "player_data", "skill2", 0)
			es.keysetvalue(login_id, "player_data", "skill3", 0)
			es.keysetvalue(login_id, "player_data", "skill4", 0)
			es.keysetvalue(login_id, "player_data", "skill5", 0)
			es.keysetvalue(login_id, "player_data", "skill6", 0)
			es.keysetvalue(login_id, "player_data", "skill7", 0)
			es.keysetvalue(login_id, "player_data", "skill8", 0)
			es.keysetvalue(login_id, "player_data", "skill9", 0)
			es.keysetvalue(login_id, "player_data", "skill10", 0)
			es.keysetvalue(login_id, "player_data", "skill11", 0)
			es.keysetvalue(login_id, "player_data", "skill12", 0)
			es.keysetvalue(login_id, "player_data", "skill13", 0)
			es.keysetvalue(login_id, "player_data", "skill14", 0)
			es.keysetvalue(login_id, "player_data", "skill15", 0)
			es.keysetvalue(login_id, "player_data", "skill16", 0)
			es.keysetvalue(login_id, "player_data", "skill17", 0)
			es.keysetvalue(login_id, "player_data", "skill18", 0)
			es.keysetvalue(login_id, "player_data", "skill19", 0)
			es.keysetvalue(login_id, "player_data", "skill20", 0)
		else:
			esc.msg("#0,255,255[Use]#255,255,255 %s : 피곤함이 몰려온다." %(username))
	if item_used == 1:
		esc.msg("#0,255,255 %s 유저#255,255,255가#gold %s 아이템#255,255,255을 사용했습니다." %(username, showname))
		keymath(steamid, "player_data", ITEM_LIST[choice]['name'], "-", 1)

def createVector(x, y, z):
    obj = spe.makeObject('Vector', spe.alloc(SIZE_VECTOR))
    obj.x = x
    obj.y = y
    obj.z = z
    return obj.base

def stet_select(userid, choice, popupname):
	steamid = es.getplayersteamid(userid)
	login_id = str(getplayerid(userid))
	if not int(es.keygetvalue(login_id, "player_data", "stetpoint")) > 0: return
	if choice == "체력":
		health = int(es.keygetvalue(login_id, "player_data", "health")) + 5
		es.keysetvalue(login_id, "player_data", "health", health)
		keymath(login_id, "player_data", "stetpoint", "-", 1)
		esc.tell(userid, " #green[스텟] #255,75,75체력을 5만큼 올렸습니다.")
	if choice == "근력":
		health = float(es.keygetvalue(login_id, "player_data", "power")) + 1
		es.keysetvalue(login_id, "player_data", "power", health)
		keymath(login_id, "player_data", "stetpoint", "-", 1)
		esc.tell(userid, " #green[스텟] #255,75,75근력을 1만큼 올렸습니다.")
	if choice == "민첩":
		health = int(es.keygetvalue(login_id, "player_data", "speed")) + 5
		es.keysetvalue(login_id, "player_data", "speed", health)
		keymath(login_id, "player_data", "stetpoint", "-", 1)
		esc.tell(userid, " #green[스텟] #75,75,255민첩을 5만큼 올렸습니다.")
	if choice == "MP":
		health = int(es.keygetvalue(login_id, "player_data", "mp")) + 1
		es.keysetvalue(login_id, "player_data", "mp", health)
		keymath(login_id, "player_data", "stetpoint", "-", 1)
		esc.tell(userid, " #green[스텟] #75,75,255MP를 1만큼 올렸습니다.")
	rpgmenu_select(userid, "스텟", "rpgmenu")

def skill_select(userid, choice, popupname):
	steamid = getplayerid(userid)
	skill_menu = popuplib.easymenu('skill_l_%s' %(userid), None, none_select)
	skill_menu.settitle("＠ %s" %(choice))
	client_skill = es.keygetvalue(steamid, "player_data", SKILL_TEST[choice]['skillname'])
	need_skillp = SKILL_TEST[choice]['need_skillp']
	max = SKILL_TEST[choice]['max']
	info = SKILL_TEST[choice]['info']
	level_info = SKILL_TEST[choice]['level_info']
	sb = SKILL_TEST[choice]['skillbook']
	if sb == -1: sbz = "없음"
	else:
		if not "unlock" in sb:
			sbz = ITEM_LIST[str(sb)]['itemrealname']
		else: sbz = "없음"
	skill_menu.setdescription(" \n＊ 필요한 스킬북 : %s\n＊ 필요한 스킬 포인트 : %s\n＊ 스킬 현황 : %s / %s\n \n%s\n%s" %(sbz, need_skillp, client_skill, max, info, level_info))
	skill_menu.addoption(choice, "%s 스킬을 익힙니다." %(choice))
	skill_menu.menuselect = learnskill_select
	skill_menu.send(userid)
	popuplib.delete('skill_l_%s' %(userid))

def learnskill_select(userid, choice, popupname):
	steamid = es.getplayersteamid(userid)
	login_id = getplayerid(userid)
	if choice != 10:
		skillpoint = es.keygetvalue(login_id, "player_data", "skillpoint")
		client_skill = int(es.keygetvalue(login_id, "player_data", SKILL_TEST[choice]['skillname']))
		skill_max = int(SKILL_TEST[choice]['max'])
		need_skillp = int(SKILL_TEST[choice]['need_skillp'])
		sb = str(SKILL_TEST[choice]['skillbook'])
		if sb == "-1": ok = 1
		else:
			if not "unlock" in str(sb):
				skillbook_get = int(es.keygetvalue(login_id, "player_data", int(ITEM_LIST[int(SKILL_TEST[choice]['skillbook'])]['name'])))
			if "unlock" in str(sb):
				skillbook_get = int(es.keygetvalue(login_id, "player_data", sb))
			if skillbook_get >= 1: ok = 2
			else: ok = 0
		for b in SKILL_TEST[choice]['nope_skill']:
			if b != "none":
				if int(es.keygetvalue(login_id, "player_data", b)) > 0: ok = 0
		if skillpoint >= client_skill:
			if skill_max > client_skill:
				if ok >= 1:
					keymath(login_id, "player_data", str(SKILL_TEST[choice]['skillname']), "+", 1)
					keymath(login_id, "player_data", "skillpoint", "-", need_skillp)
					username = es.getplayername(userid)
					esc.msg("#blue %s 유저#255,255,255가 #0,255,255%s 스킬#255,255,255을 익혔습니다." %(username, choice))
					rpgmenu_select(userid, "스킬", 0)
					if ok == 2:
						if not "unlock" in str(sb):
							esc.tell(userid, "#gold %s 스킬북 아이템#255,255,255은 소멸되었습니다." %(ITEM_LIST[int(SKILL_TEST[choice]['skillbook'])]['itemrealname']))
							keymath(login_id, "player_data", ITEM_LIST[int(SKILL_TEST[choice]['skillbook'])]['name'], "-", 1)
				else: esc.tell(userid, "#255,255,255스킬 북이 없거나 현재 스킬들의 상성에 맞지 않습니다.")
			else: esc.tell(userid, "#255,255,255스킬이 이미 MAX 상태입니다.")
		else: esc.tell(userid, "#255,255,255스킬 포인트가 모자랍니다.")

def update_svunlock():
	a = 1
	#es.keycreate("server_unlock", "de_train")
	#es.keysetvalue("server_unlock", "de_train", "unlock", 0)
	#es.keycreate("server_unlock", "de_dust2_mariostyle")
	#es.keysetvalue("server_unlock", "de_dust2_mariostyle", "unlock", 0)
	#es.keygroupsave("server_unlock", "|bot/server_data")

def es_map_start(ev):
	teleport_timer.stop()
	est.adddownload("sound/beatfeast/opening.mp3")
	es.set("say_block", 0)
	es.set("what_ent", 0)
	#---------------------------------------------------------------------------------------------------------
	#Global Variable

	global lasermodel_1
	if "_" in themap(): lasermodel_1 = es.precachemodel("effects/gunshiptracer.vmt")

	global lasermodel_2
	if "_" in themap(): lasermodel_2 = es.precachemodel("effects/laser1.vmt")

	global max_health
	max_health = {}

	global one_damage_armor
	one_damage_armor = {}

	global one_damage
	one_damage = {}

	global sayok
	sayok = {}

	global top_damage
	top_damage = {}
	top_damage['damage'] = 0
	top_damage['userid'] = 0
	#---------------------------------------------------------------------------------------------------------
	es.keygroupsave("server_unlock", "|bot/server_data")
	es.keygroupsave("total_players", "|bot/server_data")
	est.cvardelflag("sm_nextmap", 0, 0, 0, 1, 0, 0, 0, 0)
	est.cvardelflag("bot_quota", 0, 0, 0, 1, 0, 0, 0, 0)
	est.cvardelflag("mp_freezetime", 0, 0, 0, 1, 0, 0, 0, 0)
	est.cvardelflag("mp_roundtime", 0, 0, 0, 1, 0, 0, 0, 0)
	est.cvardelflag("mp_startmoney", 0, 0, 0, 1, 0, 0, 0, 0)
	est.cvardelflag("sv_tags", 0, 0, 0, 1, 0, 0, 0, 0)
	es.set("round", 1)
	currentmap = themap()
	realhost = str(sv('realhostname'))
	if currentmap in NORMAL_WORLD:
		es.server.cmd('hostname %s (Default map)' %(realhost))
	if currentmap in FAIRY_WORLD:
		es.server.cmd('hostname %s (Fairy map)' %(realhost))
	if currentmap in MONSTER_WORLD:
		es.server.cmd('hostname %s (Monster map)' %(realhost))
	if currentmap in "de_train, de_colors":
		es.server.cmd('hostname %s (Event map)' %(realhost))
	if currentmap in str(REST_MAPS):
		es.server.cmd('hostname %s (Market)' %(realhost))
	es.server.cmd('r_download "sound/zeisenproject_-1/autosounds"')
	es.server.cmd('r_download "sound/zeisenproject_-1/%s"' %(currentmap))
	if "de_" in themap():
		es.set("humanteam", 2)
		es.set("zombieteam", 3)
	else:
		if "cs_" in themap():
			es.set("humanteam", 3)
			es.set("zombieteam", 2)
		else:
			es.set("humanteam", 3)
			es.set("zombieteam", 2)
	if themap() == "de_rush_v2":
		rand_day = random.choice(["day", "night"])
		es.set("today", rand_day)
		if rand_day == "night":
			es.lightstyle(0, "c")
			es.server.cmd('sv_skyname galaxy')
	if themap() == "de_nightfever":
		rand_day = random.choice(["day", "night"])
		es.set("today", rand_day)
		if rand_day == "day":
			es.server.cmd('sv_skyname sky_day01_08')
		if rand_day == "night":
			es.lightstyle(0, "c")
		else: es.set("event_chance", 0)
	if int(sv('humanteam')) == 2:
		es.server.cmd('mp_humanteam t')
	if int(sv('humanteam')) == 3:
		es.server.cmd('mp_humanteam ct')

def round_start(ev):
	es.set("allfade", 0)
	if int(sv('round')) != 8:
		for userid in es.getUseridList():
			if not est.isalive(userid):
				est.spawn(userid)
	es.server.cmd('est4css_nosayfilter 1')
	currentmap = themap()
	BUYMENU_LIST['Be Doctor']['dollar'] = 2000
	BUYMENU_LIST['Be Doctor']['mp'] = 1
	if currentmap in FAIRY_WORLD:
		BUYMENU_LIST['Be Doctor']['dollar'] = 500
		BUYMENU_LIST['Be Doctor']['mp'] = 3
		BUYMENU_LIST['Armor + 4']['need_level'] = 1
		BUYMENU_LIST['Armor + 20']['need_level'] = 1
	if currentmap in MONSTER_WORLD:
		BUYMENU_LIST['Armor + 4']['need_level'] = 1
		BUYMENU_LIST['Armor + 20']['need_level'] = 1
	if currentmap in NORMAL_WORLD:
		BUYMENU_LIST['Armor + 4']['need_level'] = -1
		BUYMENU_LIST['Armor + 20']['need_level'] = -1
	est.remove("func_door_rotating")
	est.remove("env_explosion")
	es.set("event_line", 0)
	check = es.getuserid()
	if themap() == "de_nightfever":
		remove("func_bomb_target")
		npc_nightfever()
		es.server.cmd('bot_add_ct "[Unknown] ?"')
	if themap() == "de_rush_v2":
		remove("func_bomb_target")
		npc_rush_v2()
		npc_rush_v2()
		es.server.cmd('bot_add_ct "[Unknown] ?"')
		remove('phys_bone_follower')
	if int(sv('mp_freezetime')) == 60:
		est.stopsound("#h", "zeisenproject_-1/%s/opening.mp3" %(currentmap))
		est.play("#h", "zeisenproject_-1/%s/opening.mp3" %(currentmap))
	if int(sv('round')) == 8:
		endthegame()
		est.play("#h", "zeisenproject_-1/%s/ending.mp3" %(currentmap))
		esc.msg("#green게임이 끝났습니다. 수고하셨습니다")
		esc.msg("#green──────────────────── ")
		esc.msg("#greenGAME OVER")
		esc.msg("#green──────────────────── ")
		es.server.cmd('bot_quota 0')
		for userid in gethuman():
			if int(sv('round')) == 8:
				login_id = getplayerid(userid)
				index = est.getindex(userid)
				get_mvp = int(es.getindexprop(es.getentityindex('cs_player_manager'), 'CCSPlayerResource.m_iMVPs.%03d' %(index)))
				keymath(login_id, "player_data", "bp", "+", get_mvp)
				kill_xp = est.getkills(userid)
				assist_xp = est.getdeaths(userid)
				assist_xp = str(assist_xp)
				assist_xp = assist_xp.replace("-", "")
				if assist_xp != 0:
					assist_xp = int(assist_xp) / 2
					assist_xp = est.rounddecimal(assist_xp, 0)
				assist_xp = assist_xp.replace(".0", "")
				assist_xp = int(assist_xp)
				total_xp = int(kill_xp) + int(assist_xp)
				temp = "#0,0,0없음"
				total_xp = total_xp + (get_mvp * 17)
				if temp != "#0,0,0없음": temp = "%s + MVP(%s 경험치)" %(temp, get_mvp * 17)
				if temp == "#0,0,0없음": temp = "#goldMVP(%s 경험치)" %(get_mvp * 17)
				keymath(login_id, "player_data", "xp", "+", total_xp)
				esc.tell(userid, "#0,255,0[Round XP]#255,0,0 %s(점수)#0,255,0+#0,0,255 %s (어시스트 카운트) #0,255,0+ %s #0,255,0=#255,255,255 %s" %(kill_xp, assist_xp, temp, total_xp))
				est.killset(userid, 0)
				est.deathset(userid, 0)
	else:
		esc.msg("#255,255,255서버 오픈 시간 : %s" %(sv('server_time')))
		random_msg = random.choice(["새로운 월드를 탐험해보세요.", "직업은 추후 추가됩니다.", "밸런스 패치중입니다."])
		esc.msg("#255,255,255─┐ %s" %(random_msg))
		esc.msg("#0,255,255!메뉴로 스킬, 스텟을 익힐수 있고 인벤토리를 볼수 있습니다. J키는 상점.")
		existcheck = est.fileexists("sound/zeisenproject_-1/%s/round_start.mp3" %(currentmap))
		if existcheck == 1:
			if int(sv('mp_freezetime')) != 40: est.play("#h", "zeisenproject_-1/%s/round_start.mp3" %(currentmap))
		if int(sv('round')) == 7:
			if int(sv('mp_freezetime')) == 40:
				if themap() in NORMAL_WORLD: MAPS_LIST = NORMAL_WORLD
				if themap() in FAIRY_WORLD: MAPS_LIST = FAIRY_WORLD
				if themap() in MONSTER_WORLD: MAPS_LIST = MONSTER_WORLD
				#if random.randint(1,3) == 3:
				#	EVENT_LIST = [
				#	"de_dust2_mariostyle", "de_train"]
				#	for mapname in EVENT_LIST:
				#		MAPS_LIST.append("%s (이벤트 맵)" %(mapname))
				esc.msg("#255,255,255 10초 후 맵 투표가 시작됩니다.")
				map_vote = votelib.create('map_vote', map_vote_end, map_vote_submit)
				map_vote.setquestion("＊ 다음 맵을 선정해주세요!")
				count = 0
				max_count = 3
				ADD_LIST = []
				if themap() == "de_colors":
					max_count = 0
				if not themap() in NORMAL_WORLD:
					map_vote.addoption("de_nightfever")
					ADD_LIST.append("de_nightfever")
				while count < max_count:
					for mapname in MAPS_LIST:
						if not mapname in ADD_LIST and mapname != str(sv('eventscripts_currentmap')):
							if random.randint(1,3) == 1:
								if count < max_count:
									count += 1
									if count == 1: es.set("willmap", mapname)
									map_vote.addoption(mapname)
									ADD_LIST.append(mapname)
				gamethread.delayed(10, map_vote.start, (20))
				gamethread.delayed(10, effectsound, ("zeisenproject_-1/autosounds/startyourvoting.mp3"))
		if currentmap == "de_colors":
			es.set("level", 1)
			if est.playercount("#h") > 0:
				npc_msg("#blue[Magician] White Bird", "새로운 손님이군요... 달리실 준비는 되셨는지요?")
		if currentmap == "de_train":
			es.set("level", 10)
			if est.playercount("#h") > 0:
				npc_msg("#red[Extra] 오오타 준페이", "네가 주점을 망가뜨렸지! 당장 나와!")
				gamethread.delayed(4, npc_msg, ("#blue[Reckless] Fade", "이이잉? 왜에?"))
				gamethread.delayed(8, npc_msg, ("#blue[Reckless] Fade", "음.. 글쎄... 아, 그래. 내가 맞아! 내가 범인이야!"))
				gamethread.delayed(12, npc_msg, ("#red[Extra] 오오타 준페이", "그렇지? 당장 사과해!"))
				gamethread.delayed(16, npc_msg, ("#blue[Reckless] Fade", "그건 싫은데... 나를 이기면 그렇게 할게!"))
				gamethread.delayed(20, npc_msg, ("#blue[Reckless] Fade", "내가, 오늘 아빠한테서 선물을 받았는데 말이야-"))
				gamethread.delayed(24, npc_msg, ("#blue[Reckless] Fade", "그걸 한번 실험해 보고싶어."))
				gamethread.delayed(28, npc_msg, ("#red[Extra] 오오타 준페이", "좋아, 지면 해준다고 했지! 못할것도 없지! 해보자고!"))
		if "cs_" in themap():
			cm = es.precachemodel("models/player/reisenbot/cirno/cirno.mdl")
			hostage_list = es.createentityindexlist("hostage_entity")
			for index in hostage_list:
				es.setindexprop(index, "CBaseEntity.m_nModelIndex", cm)
				est.setentitycolor(index, 255, 255, 255, 255)
				es.setindexprop(index, "CHostage.baseclass.baseclass.baseclass.baseclass.m_flModelScale", 0.75)
				es.setindexprop(index, "CHostage.m_lifeState", 0)

def change_vote_end(votename, win, winname, winvotes, winpercent, total, tie, cancelled):
	effectsound("zeisenproject_-1/autosounds/endofvote.mp3")
	if winname == "YES YES YES":
		es.server.cmd('changelevel cs_assault2_goban_b3')

def change_vote_submit(userid, votename, choice, choicename):
	username = es.getplayername(userid)
	#esc.msg("#green[Nextmap Vote] #blue %s 유저#255,255,255는#0,255,255 %s 맵#255,255,255에 투표했습니다." %(username, choicename))
	if choicename == "YES YES YES":
		effectsound("bot/yesss2.wav")
		es.server.cmd('es_xsexec %s say YESS' %(userid))
	else:
		effectsound("bot/no.wav")
		es.server.cmd('es_xsexec %s say No.' %(userid))

def map_vote_end(votename, win, winname, winvotes, winpercent, total, tie, cancelled):
	winname = winname.replace(" (이벤트 맵)", "")
	if "_" in winname:
		effectsound("zeisenproject_-1/autosounds/endofvote.mp3")
		esc.msg("#255,255,255맵이 %s 맵으로 확정되었습니다." %(winname))
		es.server.cmd('sm_nextmap %s' %(winname))
	else:
		effectsound("zeisenproject_-1/autosounds/endofvote.mp3")
		esc.msg("#255,255,255맵이 %s 맵으로 확정되었습니다." %(sv('willmap')))
		es.server.cmd('sm_nextmap %s' %(sv('willmap')))

def map_vote_submit(userid, votename, choice, choicename):
	username = es.getplayername(userid)
	esc.msg("#green[Nextmap Vote] #blue %s 유저#255,255,255는#0,255,255 %s 맵#255,255,255에 투표했습니다." %(username, choicename))

def changemap_vote(argmap):
	if votelib.exists('change_vote'):
		if not votelib.isrunning('change_vote'):
			map_vote = votelib.create('change_vote', change_vote_end, change_vote_submit)
			map_vote.setquestion("＊ cs__assault2_goban_b3 맵으로 이동할래요?")
			map_vote.addoption("YES YES YES")
			map_vote.addoption("NO NO NO")
			map_vote.start(20)
			effectsound("zeisenproject_-1/autosounds/startyourvoting.mp3")
	else:
		map_vote = votelib.create('change_vote', change_vote_end, change_vote_submit)
		map_vote.setquestion("＊ cs__assault2_goban_b3 맵으로 이동할래요?")
		map_vote.addoption("YES YES YES")
		map_vote.addoption("NO NO NO")
		map_vote.start(20)
		effectsound("zeisenproject_-1/autosounds/startyourvoting.mp3")

def round_freeze_end(ev):
	es.set("fight", 1)
	currentmap = themap()
	round_variable = int(sv('round'))
	level_variable = int(sv('level'))
	if themap() in str(NORMAL_WORLD): es.set("zombie_count", level_variable * 3)
	if themap() in str(MONSTER_WORLD): es.set("zombie_count", level_variable * 10)
	if themap() in str(FAIRY_WORLD): es.set("zombie_count", level_variable * 100)
	if round_variable == 1: est.stopsound("#h", "zeisenproject_-1/%s/opening.mp3" %(currentmap))
	check = est.fileexists("sound/zeisenproject_-1/%s/round_start.mp3" %(currentmap))
	if check == 1: est.stopsound("#h", "zeisenproject_-1/%s/round_start.mp3" %(currentmap))
	if check == 1: est.stopsound("#h", "zeisenproject_-1/%s/round_start.mp3" %(currentmap))
	music_album = SOUNDTRACK_LIST[currentmap]['album']
	music_artist = SOUNDTRACK_LIST[currentmap]['artist']
	esc.msg("#125,125,125＊ %s ~ %s" %(music_album, music_artist))
	if int(sv('round')) == 7: esc.msg("#125,125,125＊ %s → %s" %(currentmap, sv('sm_nextmap')))
	else: esc.msg("#125,125,125＊ %s → Map Vote(7 Round)" %(currentmap))
	esc.msg("#255,0,0◎ Level %s" %(level_variable))
	if round_variable != 7: esc.msg("#0,255,0◎ %s Round" %(round_variable))
	if round_variable == 7: esc.msg("#0,255,0◎ Final Round")
	type_check = "sound/zeisenproject_-1/%s/%slevel.mp3" %(currentmap, level_variable)
	checkz = est.fileexists(type_check)
	if checkz == 1: print_mp3 = "zeisenproject_-1/%s/%slevel.mp3" %(currentmap, level_variable)
	if checkz == 0:
		print_mp3 = "zeisenproject_-1/%s/%s_stage.mp3" %(currentmap, round_variable)
		checkx = est.fileexists("sound/%s" %(print_mp3))
		if checkx == 0: print_mp3 = "NULL"
	#--------------------------------------------------------------------------------------------------------------------------------------
	if print_mp3 == "zeisenproject_-1/de_train/10level.mp3": bgm_loop.start(64, 99999)
	if themap() == "de_colors":
		print_mp3 = "zeisenproject_-1/de_colors/1level.mp3"
	if print_mp3 == "zeisenproject_-1/de_colors/1level.mp3": bgm_loop.start(142, 99999)
	#--------------------------------------------------------------------------------------------------------------------------------------
	if print_mp3 != "NULL":
		for to_userid in gethuman():
			est.play(to_userid, print_mp3)
	es.set("mmusic", print_mp3)
	#--------------------------------------------------------------------------------------------------------------------------------------
	#Custom Music
	es.server.cmd('mp_ignore_round_win_conditions 0')
	if currentmap in str(REST_MAPS):
		if str(sv('sv_password')) != "nipperkk":
			es.server.cmd('mp_ignore_round_win_conditions 1')
			if random.randint(1,10) == 7:
				rain()
			est.play("#h", "zeisenproject_-1/%s/%s.mp3" %(currentmap, sv('today')))
			es.set("mmusic", "zeisenproject_-1/%s/%s.mp3" %(currentmap, sv('today')))
			if currentmap == "de_rush_v2":
				if str(sv('today')) == "day": bgm_loop.start(190, 99999)
				if str(sv('today')) == "night": bgm_loop.start(173, 99999)
			if currentmap == "de_nightfever":
				if str(sv('today')) == "day": bgm_loop.start(158, 99999)
				if str(sv('today')) == "night": bgm_loop.start(113, 99999)

def bgm_loop():
	est.stopsound("#h", sv('mmusic'))
	gamethread.delayed(0.1, est.play, ("#h", sv('mmusic')))

def item_pickup(ev):
	userid = int(ev['userid'])
	item = str(ev['item'])
	if not es.isbot(userid):
		if item == "hegrenade":
			ammo = est.getammo(userid, item)
			if ammo > 1: est.setammo(userid, item, 1)
	else:
		username = es.getplayername(userid)
	if item == "c4":
		if themap() in "de_train, de_nightfever, de_colors":
			est.dissolve("weapon_c4")


def round_end(ev):
	es.set("fight", 0)
	bgm_loop.stop()
	winner = int(ev['winner'])
	es.set("winner", winner)
	currentmap = themap()
	round_variable = int(sv('round'))
	if int(sv('server_update')) == 1:
		es.set("server_update", 0)
		#esc.msg("#255,255,255서버를 업데이트하고 있습니다...")
		es.server.cmd('es_xdelayed 1 es_xreload bot')
	if winner > 1:
		if int(sv('round')) == 1 and int(sv('mp_freezetime')) == 60: est.stopsound("#h", "zeisenproject_-1/%s/opening.mp3" %(currentmap))
		est.stopsound("#h", "zeisenproject_-1/%s/%s_stage.mp3" %(currentmap, round_variable))
		round_variable = svmath("round", "+", 1)
		if not currentmap in SPECIAL_MAPS:
			es.server.cmd('mp_freezetime 10')
		else:
			if currentmap == "de_train": es.server.cmd('mp_freezetime 30')
			if currentmap == "de_colors": es.server.cmd('mp_freezetime 10')
		if int(sv('round')) == 7:
			es.set("mp_freezetime", 40)
		if winner == 2: est.slay("#c")
		if winner == 3: est.slay("#t")
		if winner == int(sv('zombieteam')):
			est.play("#h", "zeisenproject_-1/autosounds/defeat.mp3")
			level = svmath("level", "-", 1)
			if level <= 0:
				level = 1
				es.set("level", 1)
		if winner == int(sv('humanteam')):
			est.play("#h", "zeisenproject_-1/autosounds/win.mp3")
			level = int(sv('level'))
			if themap() in FAIRY_WORLD:
				if level <= 4:
					level = svmath("level", "+", 1)
			if themap() in MONSTER_WORLD:
				if level <= 4:
					level = svmath("level", "+", 1)
			if themap() in NORMAL_WORLD:
				if level <= 4:
					level = svmath("level", "+", 1)
			top_winner = int(top_damage['userid'])
			if themap() == "de_train":
				for a in playerlib.getPlayerList("#human"):
					if es.getplayerteam(a.userid) > 1: est.killadd(a.userid, 333)
				npc_msg("#red[Extra] 오오타 준페이", "야, 어디가?!")
				gamethread.delayed(3, npc_msg, ("#blue[Reckless] Fade", "이럴땐 도망가는거야!! 엄마!! 엄마아아아!!!"))
		top_damage['userid'] = 0
		top_damage['damage'] = 0
	else:
		if int(sv('round')) == 1:
			if int(sv('bot_quota')) == 2:
				if est.playercount("#h") > 0:
					if themap() != "de_nightfever" and not themap() in SPECIAL_MAPS:
						if themap() in NORMAL_WORLD:
							es.server.cmd('bot_add "[Human] 퀘이사"')
							es.server.cmd('bot_add "[Human] 레일라"')
							es.server.cmd('bot_add "[Human] 던 레이트"')
							es.server.cmd('bot_add "[Human] 마트 루핀"')
							es.server.cmd('bot_add "[Human] 스트레이트 킹"')
							if "de_" in themap(): es.server.cmd('bot_add "[Gunner] Camp Killer"')
							es.server.cmd('mp_freezetime 60')
							es.server.cmd('bot_quota 26')
							es.server.cmd('bot_difficulty 3')
							es.server.cmd('mp_roundtime 2.65')
						if themap() in MONSTER_WORLD:
							es.server.cmd('bot_add "[Human] 퀘이사"')
							es.server.cmd('bot_add "[Human] 레일라"')
							es.server.cmd('bot_add "[Human] 던 레이트"')
							es.server.cmd('bot_add "[Human] 마트 루핀"')
							es.server.cmd('bot_add "[Human] 스트레이트 킹"')
							es.server.cmd('bot_add "[Gunner] Elite Sniper"')
							es.server.cmd('bot_add "[Gunner] Roca"')
							count = 1
							while count <= 18:
								es.server.cmd('bot_add "[Shooter] %s"' %(count))
								count += 1
							es.server.cmd('mp_freezetime 60')
							es.server.cmd('bot_quota 99')
							es.server.cmd('bot_difficulty 1')
							es.server.cmd('mp_roundtime 3.5')
						if themap() in FAIRY_WORLD:
							es.server.cmd('bot_add "[Human] 퀘이사"')
							es.server.cmd('bot_add "[Human] 레일라"')
							es.server.cmd('bot_add "[Human] 던 레이트"')
							es.server.cmd('bot_add "[Human] 마트 루핀"')
							es.server.cmd('bot_add "[Human] 스트레이트 킹"')
							es.server.cmd('bot_add "[Bomber] ^^"')
							es.server.cmd('bot_add "[Gunner] The Sea"')
							count = 1
							while count <= 18:
								es.server.cmd('bot_add "[Flaght] %s"' %(count))
								count += 1
							es.server.cmd('mp_freezetime 60')
							es.server.cmd('bot_quota 99')
							es.server.cmd('bot_difficulty 1')
							es.server.cmd('mp_roundtime 3.5')
					else:
						if themap() == "de_train":
							es.server.cmd('bot_add "[Extra] 오오타 준페이"')
							es.server.cmd('bot_add "[Human] 레일라"')
							es.server.cmd('bot_add "[Human] 던 레이트"')
							es.server.cmd('bot_add "[Human] 마트 루핀"')
							es.server.cmd('bot_add "[Human] 스트레이트 킹"')
							es.server.cmd('mp_freezetime 60')
							es.server.cmd('bot_quota 27')
							es.server.cmd('bot_difficulty 3')
							es.server.cmd('mp_roundtime 8')
						if themap() == "de_colors":
							es.server.cmd('bot_add "[Human] 퀘이사"')
							es.server.cmd('bot_add "[Human] 레일라"')
							es.server.cmd('bot_add "[Human] 던 레이트"')
							es.server.cmd('bot_add "[Human] 마트 루핀"')
							es.server.cmd('bot_add "[Human] 스트레이트 킹"')
							es.server.cmd('mp_freezetime 60')
							es.server.cmd('bot_quota 6')
							es.server.cmd('bot_difficulty 0')
							es.server.cmd('mp_roundtime 8')
	if int(sv('round')) == 8: es.server.cmd('mp_freezetime 59')

def round_mvp(ev):
	mvp_userid = int(ev['userid'])
	'''
	for userid in playerlib.getPlayerList("#human"):
		if es.getplayerteam(userid) > 1:
			login_id = getplayerid(userid)
			kill_xp = est.getkills(userid)
			assist_xp = est.getdeaths(userid)
			assist_xp = str(assist_xp)
			assist_xp = assist_xp.replace("-", "")
			if assist_xp != 0:
				assist_xp = int(assist_xp) / 2
				assist_xp = est.rounddecimal(assist_xp, 0)
				assist_xp = assist_xp.replace(".0", "")
				assist_xp = int(assist_xp)
			difficulty = (int(sv('level')) - 1) * 2
			total_xp = int(kill_xp) + int(assist_xp) + int(difficulty)
			temp = "#0,0,0없음"
			if mvp_userid == userid:
				total_xp *= 2
				if temp != "#0,0,0없음": temp = "%s + MVP Bonus(경험치 2배)" %(temp)
				if temp == "#0,0,0없음": temp = "#goldMVP Bonus(경험치 2배)"
			keymath(login_id, "player_data", "xp", "+", total_xp)
			esc.tell(userid, "#0,255,0[Round XP]#255,0,0 %s(점수)#0,255,0+#0,0,255 %s (어시스트 카운트) #0,255,0+#0,255,255 %s (봇 난이도) #0,255,0+ %s #0,255,0=#255,255,255 %s" %(kill_xp, assist_xp, temp, total_xp)) 
	est.killset("#h", 0)
	est.deathset("#h", 0)
	'''

def hostage_follows(ev):
	userid = int(ev['userid'])
	index = est.getviewprop(userid)
	es.emitsound("entity", index, "zeisenproject_-1/autosounds/cirno_follow.mp3", 1.0, 1.0)
	es.emitsound("entity", index, "zeisenproject_-1/autosounds/cirno_follow.mp3", 1.0, 1.0)
	es.emitsound("entity", index, "zeisenproject_-1/autosounds/cirno_follow.mp3", 1.0, 1.0)
	name = es.getplayername(userid)
	if not es.isbot(userid):
		for userid in gethuman(): usermsg.hudhint(userid, "%s 유저가 인질을 구출중입니다." %(name))
	else:
		for userid in gethuman(): usermsg.hudhint(userid, "%s 봇이 인질을 구출중입니다." %(name))

def hostage_stops_following(ev):
	userid = int(ev['userid'])
	index = est.getviewprop(userid)
	es.emitsound("entity", index, "zeisenproject_-1/autosounds/cirno_stop.mp3", 1.0, 1.0)

def player_connect(ev):
	userid = int(ev['userid'])
	steamid = str(ev['networkid'])
	username = str(ev['name'])
	if steamid != "BOT":
		player_count = svmath("player_count", "+", 1)
		esc.msg("#green %s Player Connecting #lightgreen[ %s ]" %(username, player_count))

def player_disconnect(ev):
	userid = int(ev['userid'])
	steamid = str(ev['networkid'])
	username = str(ev['name'])
	reason = str(ev['reason'])
	reason = reason.replace('"', '')
	if steamid == "BOT":
		es.keygroupdelete("assist_group_%s" %(userid))
		if "server is" in reason:
			es.server.cmd('es_xsoon bot_quota 0')
	if steamid != "BOT":
		player_count = svmath("player_count", "-", 1)
		esc.msg("#darkgreen %s Player Disconnected #green[ %s ]#255,255,255(%s)" %(username, player_count, reason))
		cc = 0
		login_id = steamid.replace(":", "")
		login_id = login_id.replace("STEAM_", "")
		login_id = login_id.replace("_", "")
		if es.exists("key", login_id, "player_data"):
			es.keygroupsave(login_id, "|bot/player_data")
			es.keygroupdelete(login_id)

def player_activate(ev):
	userid = int(ev['userid'])
	steamid = es.getplayersteamid(userid)
	currentmap = themap()
	if steamid == "BOT":
		username = es.getplayername(userid)
		if username == "[Unknown] .":
			es.changeteam(userid, 1)
		else:
			if themap() == "de_nightfever":
				es.changeteam(userid, 3)
				est.spawn(userid)
	if steamid != "BOT":
		sayok[userid] = 1
		z_max[userid] = 0
		current_mp[userid] = 0
		burn_time[userid] = 0
		if not currentmap in str(REST_MAPS):
			if int(sv('mp_freezetime')) != 60:
				gamethread.delayed(0.1, es.playsound, (userid, "zeisenproject_-1/autosounds/joinserver.mp3", 1.0))
		else:
			change_team(userid, sv('humanteam'))
			est.spawn(userid)
		check = es.exists("key", "total_players", steamid)
		if check == 0:
			es.keycreate("total_players", steamid)
			es.keysetvalue("total_players", steamid, "register", 0)
			es.keysetvalue("total_players", steamid, "register_id", "0")
			es.keysetvalue("total_players", steamid, "automatic_id", "0")
			es.keysetvalue("total_players", steamid, "automatic_password", "0")
			es.keysetvalue("total_players", steamid, "volume", 1.0)
		ste = steamid.replace("STEAM_", "")
		ste = ste.replace(":", "")
		login_id = ste
		if login_id in str(BAN_LIST):
			es.server.cmd('banid 0 %s' %(userid))
			es.server.cmd('kickid %s "You are Banned"' %(userid))
		exist = es.exists('key', ste, "player_data")
		if exist == 0:
			es.keygroupload(ste, "|bot/player_data")
		exist = es.exists('key', ste, "player_data")
		if exist == 0:
			reset_player(ste)
		else:
			update_version = int(es.keygetvalue(ste, "player_data", "update_version"))
			if update_version == 1:
				update_version = keymath(ste, "player_data", "update_version", "+", 1)
				es.keysetvalue(login_id, "player_data", "count_unlock_3", 0)
				es.keysetvalue(login_id, "player_data", "count_unlock_4", 0)
				es.keysetvalue(login_id, "player_data", "count_unlock_5", 0)
				es.keysetvalue(login_id, "player_data", "count_unlock_6", 0)
				es.keysetvalue(login_id, "player_data", "count_unlock_7", 0)
				es.keysetvalue(login_id, "player_data", "count_unlock_8", 0)
				es.keysetvalue(login_id, "player_data", "count_unlock_9", 0)
				es.keysetvalue(login_id, "player_data", "count_unlock_10", 0)
				es.keysetvalue(login_id, "player_data", "count_unlock_11", 0)
				es.keysetvalue(login_id, "player_data", "count_unlock_12", 0)
				es.keysetvalue(login_id, "player_data", "count_unlock_13", 0)
				es.keysetvalue(login_id, "player_data", "count_unlock_14", 0)
				es.keysetvalue(login_id, "player_data", "count_unlock_15", 0)
				es.keysetvalue(login_id, "player_data", "count_unlock_16", 0)
				es.keysetvalue(login_id, "player_data", "count_unlock_17", 0)
				es.keysetvalue(login_id, "player_data", "count_unlock_18", 0)
				es.keysetvalue(login_id, "player_data", "count_unlock_19", 0)
				es.keysetvalue(login_id, "player_data", "count_unlock_20", 0)
			if update_version == 2:
				update_version = keymath(ste, "player_data", "update_version", "+", 1)
				es.keysetvalue(login_id, "player_data", "play_time", 0)
			if update_version == 3:
				update_version = keymath(ste, "player_data", "update_version", "+", 1)
				es.keysetvalue(login_id, "player_data", "item5", 0)
		if currentmap in str(REST_MAPS):
			index = es.getentityindex("func_precipitation")
			if index > 0:
				trrr = random.randint(1,4)
				est.play(userid, "ambient/atmosphere/thunder%s.wav" %(trrr))
				est.play(userid, "ambient/water/water_flow_loop1.wav", 9999999, 0.25)
			if str(sv('sv_password')) != "nipperkk":
				est.play(userid, sv('mmusic'))
		if int(sv('mp_freezetime')) == 60:
			check_file = est.fileexists("sound/zeisenproject_-1/%s/opening.mp3" %(currentmap))
			if check_file == 1: est.play(userid, "zeisenproject_-1/%s/opening.mp3" %(currentmap))

def grenade_bounce(ev):
	userid = ev['userid']
	e_x = ev['x']
	e_y = ev['y']
	e_z = ev['z']
	steamid = es.getplayersteamid(userid)
	if steamid == "BOT":
		username = es.getplayername(userid)
		if username == "[Reckless] Fade":
			fuck = es.createentityindexlist("hegrenade_projectile")
			index = 0
			for f_index in fuck:
				source = es.getindexprop(f_index, "CBaseEntity.m_vecOrigin").split(",")
				if source[0] == e_x:
					if source[1] == e_y:
						if source[2] == e_z:
							index = f_index
			if index > 0:
				for a in playerlib.getPlayerList("#all,#alive"):
					if es.getplayerteam(a.userid) == int(sv('zombieteam')):
						est.god(a.userid, 1)
						gamethread.delayed(0.05, est.god, (a.userid, 0))
				es.server.cmd('es_xgive %s env_explosion' %(userid))
				last_give = int(sv('eventscripts_lastgive'))
				es.entitysetvalue(last_give, "classname", "team_explosion")
				wide = 1000
				damage = 500
				es.server.cmd('es_xfire %s team_explosion addoutput "imagnitude %s\"' % (userid, wide))
				es.server.cmd('es_xfire %s team_explosion addoutput "iradiusoverride %s\"' % (userid, damage))
				et = int(es.getplayerhandle(userid))
				es.setindexprop(last_give, 'CBaseEntity.m_hOwnerEntity', et)
				est.entteleport(last_give, e_x, e_y, e_z)
				es.server.cmd('es_xfire %s team_explosion explode' % userid)
				es.emitsound('entity', index, 'ambient/explosions/explode_%s.wav' % random.randint(1, 8), 1.0, 0.85)

def pre_player_hurt(ev):
	attacker = int(ev['attacker'])
	if attacker == 0:
		return
	userid = int(ev['userid'])
	dmg_health = int(ev['dmg_health'])
	dmg_armor = int(ev['dmg_armor'])
	weapon = str(ev['weapon'])
	hitgroup = int(ev['hitgroup'])
	health = es.getplayerprop(userid, _healthprop) + dmg_health
	es.setplayerprop(userid, _healthprop, health)
	armor = es.getplayerprop(userid, _armorprop) + dmg_armor
	es.setplayerprop(userid, _armorprop, armor)
	if es.isbot(attacker):
		attackername = es.getplayername(attacker)
		if attackername == "[Bomber] ^^":
			if attacker == userid: dmg_health = 0
		if "[Human]" in attackername:
			if attackername != "[Human] 퀘이사":
				dmg_health = dmg_health / 2
				dmg_health = est.rounddecimal(dmg_health, 0)
				dmg_health = dmg_health.replace(".0", "")
				dmg_health = int(dmg_health)
			else:
				dmg_health *= 1.5
				dmg_health = est.rounddecimal(dmg_health, 0)
				dmg_health = dmg_health.replace(".0", "")
				dmg_health = int(dmg_health)
		the_armor = est.getarmor(userid)
		if the_armor > 0:
			the_armor -= dmg_health
			dmg_armor += dmg_health
			dmg_health = 0
			if the_armor < 0:
				tt = str(the_armor)
				dmg_health = tt.replace("-", "")
				dmg_health = int(dmg_health)
				the_armor = 0
			est.setarmor(userid, the_armor)
			x,y,z = es.getplayerlocation(userid)
			es.server.cmd('est_effect_14 %s 0 sprites/strider_blackball.vmt %s,%s,%s %s,%s,%s 100 10 50' %(attacker, x, y, z, x, y, z))
		if not "[Normal]" in attackername:
			if not "[Shooter]" in attackername:
				if not "[Flaght]" in attackername:
					if not attackername in "[Gunner] Roca":
						dmg_health *= 2
		if attackername == "[Gunner] Slayer":
			dmg_health *= 1.75
		if attackername == "[Gunner] Camp Killer":
			dmg_health = 5
		if attackername == "[Rage] Ivas":
			r,g,b,a = getplayercolor(attacker)
			if r == 255 and g == 255 and b == 0:
			 	dmg_health *= 2
			if r == 255 and g == 0 and b == 0:
			 	dmg_health *= 4
	if "explosion" in weapon:
		if es.isbot(userid):
			username = es.getplayername(userid)
			if "[Gunner]" in username:
				dmg_health = 0
	if not es.isbot(attacker):
		attackersteamid = es.getplayersteamid(attacker)
		if attackersteamid == "STEAM_0:0:38622202":
			dmg_health *= 0.25
		login_id = getplayerid(attacker)
		mastery = str(es.keygetvalue(login_id, "player_data", "mastery"))
		if mastery == "용병(AR) ":
			if weapon in "galil, famas, m4a1, ak47, sg552, aug":
				dmg_health *= 1.5
		if est.getgun(userid) == "weapon_knife":
			if weapon == "xm1014":
				dmg_health *= 1.25
			if weapon == "scout" or weapon == "awp":
				dmg_health *= 1.65
		if weapon == "sg550" or weapon == "g3sg1":
			dmg_health *= 0.1
		if weapon == "knife":
			if onGround(userid) == 0:
				skill = int(es.keygetvalue(login_id, "player_data", "skill5"))
				if skill:
					dmg_health = dmg_health + dmg_health * (skill * 0.1)
		skill = int(es.keygetvalue(login_id, "player_data", "skill3"))
		if skill:
			if not weapon in "hegrenade, flashbang, smokegrenade, knife":
				gc = est.getclipammo(attacker, weapon)
				if gc == 0:
					dmg_health = dmg_health + dmg_health * (skill * 0.2)
		if weapon == "hegrenade":
			if est.getgun(userid) == "weapon_knife":
				dmg_min = int(es.keygetvalue(login_id, "player_data", "hegrenade_damage_min"))
				dmg_max = int(es.keygetvalue(login_id, "player_data", "hegrenade_damage_max"))
				dmg_random = random.randint(dmg_min, dmg_max) + dmg_health
				dmg_health = dmg_random
				if mastery == "봄버맨 ": dmg_health *= 0.2
			else: dmg_health *= 0.65
		if weapon != "knife": es.playsound(attacker, "weapons/crossbow/hit1.wav", 1.0)
		else:
			dmg_health *= 5
			es.playsound(attacker, "weapons/crossbow/hitbod%s.wav" %(random.randint(1,2)), 1.0)
		power = float(es.keygetvalue(login_id, "player_data", "power")) / 100
		dmg_health *= power
		dmg_health = est.rounddecimal(dmg_health, 0)
		dmg_health = dmg_health.replace(".0", "")
		dmg_health = int(dmg_health)
		if es.isbot(userid):
			the_armor = est.getarmor(userid)
			if the_armor > 0:
				the_armor -= dmg_health
				dmg_armor += dmg_health
				dmg_health = 0
				if the_armor < 0:
					tt = str(the_armor)
					dmg_health = tt.replace("-", "")
					dmg_health = int(dmg_health)
					the_armor = 0
				est.setarmor(userid, the_armor)
				x,y,z = es.getplayerlocation(userid)
				x = est.rounddecimal(x, 2)
				y = est.rounddecimal(y, 3)
				z = est.rounddecimal(z, 3)
				es.server.cmd('est_effect_14 %s 0 sprites/strider_blackball.vmt %s,%s,%s %s,%s,%s 100 10 50' %(attacker, x, y, z, x, y, z))
			if dmg_health > 0:
				check = es.exists("key", "assist_group_%s" %(userid), attackersteamid)
				if check == 0:
					es.keycreate("assist_group_%s" %(userid), attackersteamid)
					es.keysetvalue("assist_group_%s" %(userid), attackersteamid, "dmg_health", dmg_health)
				else: keymath("assist_group_%s" %(userid), attackersteamid, "dmg_health", "+", dmg_health)
			else:
				if dmg_armor > 0:
					check = es.exists("key", "assist_group_%s" %(userid), attackersteamid)
					if check == 0:
						es.keycreate("assist_group_%s" %(userid), attackersteamid)
						es.keysetvalue("assist_group_%s" %(userid), attackersteamid, "dmg_health", dmg_armor)
					else: keymath("assist_group_%s" %(userid), attackersteamid, "dmg_health", "+", dmg_armor)
		one_damage_armor[attacker] = int(one_damage_armor[attacker]) + dmg_armor
		one_damage[attacker] = int(one_damage[attacker]) + dmg_health
		health = es.getplayerprop(userid, _healthprop) - dmg_health
		armor = est.getarmor(userid)
		username = es.getplayername(userid)
		if dmg_health > 0:
			usermsg.centermsg(attacker, "%s\n- %s HP (%s/%s)" %(username, one_damage[attacker], health, max_health[userid]))
		else:
			usermsg.centermsg(attacker, "%s\n- %s AP [%s]" %(username, one_damage_armor[attacker], armor))
		est.cashadd(attacker, dmg_health / 2)
		gamethread.delayed(0.025, one_damage_armor_reset, (attacker))
		gamethread.delayed(0.025, one_damage_reset, (attacker))
	if not es.isbot(userid):
		the_armor = est.getarmor(userid)
		if the_armor > 0:
			the_armor -= dmg_health
			dmg_armor += dmg_health
			dmg_health = 0
			if the_armor < 0:
				tt = str(the_armor)
				dmg_health = tt.replace("-", "")
				dmg_health = int(dmg_health)
				the_armor = 0
			est.setarmor(userid, the_armor)
			x,y,z = es.getplayerlocation(userid)
			x = est.rounddecimal(x, 2)
			y = est.rounddecimal(y, 3)
			z = est.rounddecimal(z, 3)
			es.server.cmd('est_effect_14 %s 0 sprites/strider_blackball.vmt %s,%s,%s %s,%s,%s 100 10 50' %(userid, x, y, z, x, y, z))
	if es.isbot(userid):
		username = es.getplayername(userid)
		if username == "[Gunner] Elite Shooter":
			est.setaim(userid, attacker, 0)
		if dmg_health >= 100:
			if username == "[Reckless] Fade":
				if int(sv('event_line')) >= 3:
					if int(sv('event_line')) == 3:
						es.server.cmd('es_xsexec %s use weapon_usp' %(userid))
					else:
						est.removeweapon(userid, 3)
						check = est.getweaponindex(userid, "weapon_hegrenade")
						if check == 0: es.server.cmd('es_xgive %s weapon_hegrenade' %(userid))
						es.server.cmd('es_xdelayed 0.2 es_xsexec %s use weapon_hegrenade' %(userid))
	health = int(es.getplayerprop(userid, _healthprop)) - dmg_health
	es.setplayerprop(userid, _healthprop, health)

def player_hurt(ev):
	userid = int(ev['userid'])
	attacker = int(ev['attacker'])
	dmg_health = int(ev['dmg_health'])
	if attacker == 0:
		if es.isbot(userid):
			health = int(es.getplayerprop(userid, _healthprop)) + dmg_health
			es.setplayerprop(userid, _healthprop, health)
	if attacker != 0:
		weapon = str(ev['weapon'])
		health = int(es.getplayerprop(userid, _healthprop))
		attackerhealth = int(es.getplayerprop(attacker, _healthprop))
		if es.isbot(attacker):
			attackername = es.getplayername(attacker)
			if attackername == "[Bulldozer] Templer":
				if weapon == "knife":
					est.setaim(attacker, userid, 0)
					knockback = 200
					knockback *= int(ev['dmg_health'])
					x, y, z = playerlib.getPlayer(attacker).get('viewvector')
					es.setplayerprop(userid, 'CBasePlayer.localdata.m_vecBaseVelocity', '%s,%s,%s'%(x * knockback, y * knockback, z * knockback))
					es.setplayerprop(attacker, 'CBasePlayer.localdata.m_vecBaseVelocity', '%s,%s,%s'%(x * knockback, y * knockback, z * knockback))
					es.emitsound("player", userid, "weapons/underwater_explode3.wav", 1.0, 1.0)
					es.emitsound("player", userid, "weapons/underwater_explode3.wav", 1.0, 1.0)
					es.emitsound("player", userid, "weapons/underwater_explode3.wav", 1.0, 1.0)
					xx,yy,zz = es.getplayerlocation(userid)
					es.server.cmd('est_effect 11 #a 0 sprites/redglow1.vmt %s %s %s 2 5 255' %(xx,yy,zz))
					es.server.cmd('est_effect 10 #a 0 sprites/laser.vmt %s %s %s 100 300 1 10 100 0 255 5 5 255 1' %(xx,yy,zz))
					es.server.cmd('est_effect 11 #a 0 sprites/combineball_trail_red_1.vmt %s %s %s 2 8 255' %(xx,yy,zz))
		if not es.isbot(userid):
			me_health = est.gethealth(userid)
			me_armor = est.getarmor(userid)
			usermsg.hudmsg(userid, "HP %s│AP %s" %(me_health, me_armor), 0, 0.02, 0.93, r1=0)
			est.fade(userid, 0, 0.03, 0.03, 255, 0, 0, 75)
		if not es.isbot(attacker):
			login_id = getplayerid(attacker)
			mastery = str(es.keygetvalue(login_id, "player_data", "mastery"))
			#if weapon == "knife":
			#	if mastery == "아이언 맨 ":
			#		random_sound = random.randint(1,3)
			#		IRON_MAN[attacker] = random_sound
			#		es.emitsound("player", attacker, "zeisenproject_-1/autosounds/ironman_%s.wav" %(random_sound), 1.0, 1.0)
		if es.isbot(userid):
			username = es.getplayername(userid)
			if "[Normal]" in username: es.emitsound("player", userid, "npc/zombie/zombie_pain%s.wav" %(random.randint(1,6)), 1.0, 0.5)
			else: es.setplayerprop(userid, "CCSPlayer.cslocaldata.m_flVelocityModifier", 1)
			if username == "[Magician] White Bird":
				RANDOM_MODEL = random.choice(["player/slow/me2/geth_trooper/slow.mdl",
				"player/slow/section_8/slow.mdl", "models/player/techknow/paranoya/paranoya.mdl",
				"player/hhp227/miku/miku", "player/knifelemon/tenko", "player/hhp227/miku/miku",
				"player/konata/idol/idol", "player/konata/zatsunemiku/zatsunemiku", "player/slow/eve/slow.mdl", "player/t_leet"])
				est.setmodel(userid, RANDOM_MODEL)
				est.setplayercolor(userid, random.randint(0,255), random.randint(0,255), random.randint(0,255), random.randint(0,255))
				est.speed(userid, float(random.randint(100,165)) / 100)
				xx,yy,zz = es.getplayerlocation(userid)
				xxx,yyy,zzz = es.getplayerlocation(attacker)
				if float(zz) < float(zzz):
					knockback = -6
					knockback *= int(ev['dmg_health'])
					x, y, z = playerlib.getPlayer(userid).get('viewvector')
					es.setplayerprop(attacker, 'CBasePlayer.localdata.m_vecBaseVelocity', '%s,%s,%s'%(x * knockback, y * knockback, z * knockback))
				else:
					if not any(es.getplayermovement(attacker)):
						if not es.isbot(attacker):
							est.makeentity('prop_physics', 'props_c17/oildrum001_explosive', xxx, yyy, zzz)
							centermsg("%s씨. 달리는걸 즐기지 못하시나요? 실격입니다!" %(es.getplayername(attacker)))
			if username == "[Gunner] Elite Killer":
				gamethread.delayed(1, est.sethealth, (userid, 150))
			if username == "[Gunner] Elite Shooter":
				gamethread.delayed(1, est.sethealth, (userid, 100))
			if username == "[Gunner] Elite Hunter":
				gamethread.delayed(1, est.sethealth, (userid, 999))
			#if not username in "[Bulldozer] Templer" and not "[Human]" in username:
			#	if getdistance(userid, attacker) <= 6:
			#		es.server.cmd('es_xsexec %s sm_wiggle' %(userid))
			if not "[Normal]" in username:
				if dmg_health >= 100:
					if getdistance(userid, attacker) <= 6:
						est.setaim(userid, attacker, 0)
			if username == "[Reckless] Fade":
				el = int(sv('event_line'))
				if el == 5:
					if health <= 9999:
						el = svmath("event_line", "+", 1)
						boss_skill("#blue[Reckless] Fade", "#125,255,125촉진 부작용")
						es.setplayerprop(userid, _speedprop, 2)
				if el == 4:
					if health <= 25000:
						el = svmath("event_line", "+", 1)
						boss_skill("#blue[Reckless] Fade", "#125,255,125진실과 거짓의 관계")
						for a in playerlib.getPlayerList("#dead"):
							est.spawn(a.userid)
				if el == 3:
					if health <= 50000:
						el = svmath("event_line", "+", 1)
						boss_skill("#blue[Reckless] Fade", "#125,255,125아빠가 준 마지막 선물")
				if el == 2:
					if health <= 75000:
						el = svmath("event_line", "+", 1)
						boss_skill("#blue[Reckless] Fade", "#125,255,125아빠가 들려준 세상의 이야기")
				if el == 1:
					if health <= 90000:
						el = svmath("event_line", "+", 1)
						boss_skill("#blue[Reckless] Fade", "#125,255,125아이가 바라본 집의 풍경")
						for a in playerlib.getPlayerList("#bot,#dead"):
							if es.getplayerteam(a.userid) == int(sv('zombieteam')):
								est.spawn(a.userid)
				if el == 0:
					if health <= 5000:
						el = svmath("event_line", "+", 1)
						boss_skill("#blue[Reckless] Fade", "#125,255,125성장 촉진제")
						es.setplayerprop(userid, _healthprop, 100000)
						max_health[userid] = 100000
						es.setplayerprop(userid, _speedprop, 1.5)
			if username == "[Rage] Ivas":
				r,g,b,a = getplayercolor(userid)
				if float(health) <= float(max_health[userid] / 2):
					if r == 255 and g == 255 and b == 255:
						est.setplayercolor(userid, 255, 255, 0, 255)
						level_variable = int(sv('level'))
						speed_much = (0.1 + level_variable * 0.05)
						speedadd(userid, speed_much)
						esc.msg("#red[Rage] Ivas 보스#255,255,255가 #yellow분노#255,255,255를 시전했습니다! #green(Speed + %s, Damage x2)" %(speed_much))
				if float(health) <= float(max_health[userid] / 4):
					if r == 255 and g == 255 and b == 0:
						est.setplayercolor(userid, 255, 0, 0, 255)
						level_variable = int(sv('level'))
						speed_much = (0.15 + level_variable * 0.07)
						speedadd(userid, speed_much)
						esc.msg("#red[Rage] Ivas 보스#255,255,255가 #255,0,0분노#255,255,255를 시전했습니다! #green(Speed + %s, Damage x4)" %(speed_much))

def bot_away(userid, x, y, z):
	loc = (x, y, z)
	vec_ptr = createVector(*loc)
	spe.call('MoveAway', spe.getPlayer(userid), vec_ptr)
	spe.dealloc(vec_ptr)

def weapon_fire(ev):
	userid = int(ev['userid'])
	steamid = es.getplayersteamid(userid)
	weapon = str(ev['weapon'])
	weapon_index = est.getweaponindex(userid, weapon)
	if steamid != "BOT":
		r,g,b,a = getentitycolor(weapon_index)
		me_clip = est.getclipammo(userid, weapon)
		me_ammo = est.getammo(userid, weapon)
		me_cash = es.getplayerprop(userid, _moneyprop)
		usermsg.hudmsg(userid, "%s Cash\n%s/%s" %(me_cash, me_clip, me_ammo), 1, 0.9, 0.93, r1=r, g1=g, b1=b)
		login_id = getplayerid(userid)
		mastery = str(es.keygetvalue(login_id, "player_data", "mastery"))
		if mastery == "#85,255,255체인 ":
			es.setplayerprop(userid, "CCSPlayer.cslocaldata.m_iShotsFired", 1)
			es.setindexprop(weapon_index, "CBaseCombatWeapon.LocalActiveWeaponData.m_flNextPrimaryAttack", 0)
			es.setindexprop(weapon_index, "CBaseCombatWeapon.LocalActiveWeaponData.m_flNextSecondaryAttack", 0)
			es.setindexprop(weapon_index, "CBaseCombatWeapon.m_fAccuracyPenalty", 0)
			es.setindexprop(weapon_index, "CBaseCombatWeapon.m_fWeaponMode", 3)
			es.setplayerprop(userid, "CBasePlayer.localdata.m_Local.m_vecPunchAngle", "0,0,0")
		if not weapon in "hegrenade, flashbang, smokegrenade, knife":
			r,g,b,a = getweaponcolor(weapon_index)
			if r == 0 and g == 255 and b == 0:
				es.setindexprop(weapon_index, "CWeaponM4A1.baseclass.baseclass.m_fAccuracyPenalty", 0.0)
				es.setindexprop(weapon_index, "CWeaponCSBaseGun.baseclass.m_fAccuracyPenalty", 0.0)
				es.setindexprop(weapon_index, "CWeaponCSBaseGun.baseclass.m_weaponMode", 1)
				#es.setplayerprop(userid, "CBasePlayer.localdata.m_Local.m_vecPunchAngle", "0,0,0")
			if r == 0 and g == 0 and b == 255:
				est.setclipammo(userid, weapon, 99)
		if weapon == "hegrenade":
			#es.server.cmd('es_xsexec %s use weapon_hegrenade' %(userid))
			es.setindexprop(weapon_index, "CHEGrenade.baseclass.baseclass.baseclass.LocalActiveWeaponData.m_flTimeWeaponIdle", 0)
			es.setindexprop(weapon_index, "CBaseCombatWeapon.LocalActiveWeaponData.m_flNextPrimaryAttack", 0)
			es.setindexprop(weapon_index, "CBaseCombatWeapon.LocalActiveWeaponData.m_flNextSecondaryAttack", 0)
			es.setplayerprop(userid, "CCSPlayer.baseclass.baseclass.bcc_localdata.m_flNextAttack", 0)
		if weapon == "knife":
			swing_sound = "weapons/iceaxe/iceaxe_swing1.wav"
			if themap() in str(REST_MAPS):
				if int(es.keygetvalue(login_id, "player_data", "item1")) > 0:
					propid = est.getviewprop(userid)
					prop_name = es.entitygetvalue(propid, "classname")
					if prop_name == "player":
						prop_userid = -1
						for a_userid in gethuman():
							inde = es.getindexfromhandle(es.getplayerhandle(a_userid))
							if inde == propid:
                                                                prop_userid = a_userid
                                                                break
						if prop_userid > 0:
							if getdistance(userid, prop_userid) <= 2.5:
								knockback = 400
								x,y,z = playerlib.getPlayer(userid).get('viewvector')
								es.server.cmd('damage %s 10 32 %s' %(prop_userid, userid))
								es.setplayerprop(prop_userid, 'CBasePlayer.localdata.m_vecBaseVelocity', '%s,%s,%s'%(x * knockback * 2, y * knockback * 2, z * knockback * 4))
					swing_sound = "weapons/stunstick/stunstick_impact1.wav"
				else:
					if int(es.getplayerprop(userid, "CCSPlayer.baseclass.localdata.m_nWaterLevel")) > 0:
						propid = est.getviewprop(userid)
						prop_name = es.entitygetvalue(propid, "classname")
						if prop_name == "player":
							prop_userid = -1
							for a_userid in gethuman():
								inde = es.getindexfromhandle(es.getplayerhandle(a_userid))
								if inde == propid: prop_userid = a_userid
							if prop_userid > 0:
								if getdistance(userid, prop_userid) <= 2.5:
									knockback = 400
									x,y,z = playerlib.getPlayer(userid).get('viewvector')
									es.server.cmd('damage %s 5 32 %s' %(prop_userid, userid))
									es.setplayerprop(prop_userid, 'CBasePlayer.localdata.m_vecBaseVelocity', '%s,%s,%s'%(x * knockback * 2, y * knockback * 2, z * knockback * 4))
			es.emitsound("player", userid, swing_sound, 1.0, 1.0)
	if steamid == "BOT":
		es.setplayerprop(userid, "CCSPlayer.cslocaldata.m_iShotsFired", 0)
		if weapon == "glock":
			es.setindexprop(weapon_index, "CWeaponGlock.m_bBurstMode", 1)
		username = es.getplayername(userid)
		if weapon == "hegrenade":
			es.server.cmd('es_xdelayed 0.1 es_xgive %s weapon_hegrenade' %(userid))
			es.server.cmd('es_xdelayed 0.1 es_xsexec %s use weapon_hegrenade' %(userid))
		if "[Human]" in username:
			if username != "[Human] 퀘이사":
				fm = est.getammo(userid, weapon) + 1
				est.setammo(userid, weapon, fm)
			else:
				fm = est.getclipammo(userid, weapon) + 1
				est.setclipammo(userid, weapon, fm)
				es.setplayerprop(userid, "CBasePlayer.localdata.m_Local.m_vecPunchAngle", "0,0,0")
		if "[Extra]" in username:
			fm = est.getclipammo(userid, weapon) + 1
			est.setclipammo(userid, weapon, fm)
		if username == "[Reckless] Fade":
			if weapon == "hegrenade":
				es.server.cmd('es_xdelayed 0.2 es_xgive %s weapon_hegrenade' %(userid))
				es.server.cmd('es_xdelayed 1 es_xsexec %s use weapon_hegrenade' %(userid))
		if username == "[Gunner] Camp Killer":
			est.setclipammo(userid, weapon, 999)
			est.setammo(userid, weapon, 0)
			es.setindexprop(weapon_index, "CWeaponCSBaseGun.baseclass.m_fAccuracyPenalty", 0.0)
			es.setindexprop(weapon_index, "CWeaponCSBaseGun.baseclass.m_weaponMode", 1)
			es.setplayerprop(userid, "CBasePlayer.localdata.m_Local.m_vecPunchAngle", "0,0,0")
		if "[Gunner]" in username:
			est.setclipammo(userid, weapon, 999)
			est.setammo(userid, weapon, 0)
			es.setindexprop(weapon_index, "CWeaponCSBaseGun.baseclass.m_fAccuracyPenalty", 0.0)
			es.setindexprop(weapon_index, "CWeaponCSBaseGun.baseclass.m_weaponMode", 1)
			es.setplayerprop(userid, "CBasePlayer.localdata.m_Local.m_vecPunchAngle", "0,0,0")
		if username == "[Gunner] Elite Shooter":
			est.setclipammo(userid, weapon, 101)
			est.setammo(userid, weapon, 999)
			es.setindexprop(weapon_index, "CWeaponCSBaseGun.baseclass.m_fAccuracyPenalty", 0.0)
			es.setindexprop(weapon_index, "CWeaponCSBaseGun.baseclass.m_weaponMode", 1)
			es.setplayerprop(userid, "CBasePlayer.localdata.m_Local.m_vecPunchAngle", "0,0,0")
			est.setentitycolor(weapon_index, 0, 255, 0, 255)
		if username == "[Gunner] 하까나이":
			est.setclipammo(userid, weapon, 101)
			est.setammo(userid, weapon, 999)
			es.setindexprop(weapon_index, "CWeaponCSBaseGun.baseclass.m_fAccuracyPenalty", 0.0)
			es.setindexprop(weapon_index, "CWeaponCSBaseGun.baseclass.m_weaponMode", 1)
			es.setplayerprop(userid, "CBasePlayer.localdata.m_Local.m_vecPunchAngle", "0,0,0")
			est.setentitycolor(weapon_index, 0, 255, 0, 255)
		if username == "[Unknown] Crizi":
			est.setclipammo(userid, weapon, 256)
			es.setindexprop(weapon_index, "CBaseCombatWeapon.LocalActiveWeaponData.m_flNextPrimaryAttack", 0)
			es.setindexprop(weapon_index, "CBaseCombatWeapon.LocalActiveWeaponData.m_flNextSecondaryAttack", 0)
			es.setindexprop(weapon_index, "CBaseCombatWeapon.m_fAccuracyPenalty", 0)
			es.setindexprop(weapon_index, "CBaseCombatWeapon.m_fWeaponMode", 3)
			es.setplayerprop(userid, "CBasePlayer.localdata.m_Local.m_vecPunchAngle", "0,0,0")
		if username in "[Gunner] Elite Hunter, [Gunner] Roca":
			est.setclipammo(userid, weapon, 999)
			est.setammo(userid, weapon, 0)
			es.setindexprop(weapon_index, "CBaseCombatWeapon.LocalActiveWeaponData.m_flNextPrimaryAttack", 0)
			es.setindexprop(weapon_index, "CBaseCombatWeapon.LocalActiveWeaponData.m_flNextSecondaryAttack", 0)
			es.setplayerprop(userid, "CBasePlayer.localdata.m_Local.m_vecPunchAngle", "0,0,0")

def player_jump(ev):
	userid = int(ev['userid'])
	steamid = es.getplayersteamid(userid)
	speed = float(es.getplayerprop(userid, _speedprop))
	if steamid != "BOT":
		est.setgravity(userid, (1 / speed))
		login_id = getplayerid(userid)
		jump_count = es.keygetvalue(login_id, "player_data", "jump_count")
		keymath(login_id, "player_data", "jump_count", "+", 1)
	if steamid == "BOT":
		est.setgravity(userid, 0.5)
		x,y,z = es.getplayerlocation(userid)
		v1 = "%s,%s,%s" %(x,y,z)
		vx,vy,vz = playerlib.getPlayer(userid).viewVector()
		vx = vx * 100
		vy = vy * 100
		vz = (vz * 100) + 100
		vv = "%s,%s,%s" %(vx, vy, vz)
		es.setplayerprop(userid, "CCSPlayer.baseclass.localdata.m_vecBaseVelocity", vv)
def bullet_impact(ev):
	userid = int(ev['userid'])
	steamid = es.getplayersteamid(userid)
	event_x = ev['x']
	event_y = ev['y']
	event_z = ev['z']
	weapon = est.getgun(userid)
	if steamid == "BOT":
		x,y,z = es.getplayerlocation(userid)
		lasermodel = lasermodel_2
		z += 50
		v1 = "%s,%s,%s" %(x, y, z)
		v2 = "%s,%s,%s" %(event_x, event_y, event_z)
		username = es.getplayername(userid)
		if username == "[Gunner] Elite Killer":
			es.effect("beam", v1, v2, lasermodel, lasermodel, 0, 0, 0.2, 1, 1, 0, 1, 1, 0, 0, 255, 1)
		if username == "[Gunner] Elite Hunter":
			es.effect("beam", v1, v2, lasermodel, lasermodel, 0, 0, 0.2, 1, 1, 0, 1, 255, 0, 0, 255, 1)
		if username == "[Gunner] Elite Shooter":
			es.effect("beam", v1, v2, lasermodel, lasermodel, 0, 0, 0.2, 1, 1, 0, 1, 0, 255, 0, 255, 1)
		if username == "[Gunner] Camp Killer":
			es.effect("beam", v1, v2, lasermodel, lasermodel, 0, 0, 0.2, 1, 1, 0, 1, 255, 255, 255, 255, 1)
		if "[Human]" in username:
			es.effect("beam", v1, v2, lasermodel, lasermodel, 0, 0, 0.2, 1, 1, 0, 1, 100, 100, 255, 255, 1)
	if steamid != "BOT":
		x,y,z = es.getplayerlocation(userid)
		lasermodel = lasermodel_1
		z += 50
		v1 = "%s,%s,%s" %(x, y, z)
		v2 = "%s,%s,%s" %(event_x, event_y, event_z)
		r,g,b,a = getweaponcolor(est.getweaponindex(userid, weapon))
		me_clip = est.getclipammo(userid, weapon)
		login_id = getplayerid(userid)
		if me_clip == 0:
			if int(es.keygetvalue(login_id, "player_data", "skill3")):
				r = 0
				g = 255
				b = 255
				#event_x = est.rounddecimal(event_x, 2)
				#event_y = est.rounddecimal(event_y, 2)
				#event_z = est.rounddecimal(event_z, 2)
				#es.server.cmd('est_effect 11 %s 0 effects/rollerglow.vmt %s %s %s 0.4 0.2 255' %(userid, event_x, event_y, event_z))
		es.effect("beam", v1, v2, lasermodel, lasermodel, 0, 0, 0.2, 1, 1, 0, 1, r, g, b, a, 1)

def player_death(ev):
	userid = int(ev['userid'])
	if int(sv('round')) == 8: est.spawn(userid)
	attacker = int(ev['attacker'])
	es.remove("hat_%s" %(userid))
	if not es.isbot(userid):
		if themap() in str(REST_MAPS):
			if str(sv('sv_password')) == "nipperkk":
				es.server.cmd('kickid %s' %(userid))
				es.emitsound("player", userid, "npc/stalker/go_alert2a.wav", 1.0, 1.0)
				es.emitsound("player", userid, "npc/stalker/go_alert2a.wav", 1.0, 1.0)
			else: esc.tell(userid, "#255,255,255당신은 죽었습니다! N키를 누르면 부활할수 있습니다.")
		login_id = getplayerid(userid)
		keymath(login_id, "player_data", "death", "+", 1)
		est.deathadd(userid, -1)
	if not es.isbot(attacker):
		weapon = str(ev['weapon'])
		login_id = getplayerid(attacker)
		keymath(login_id, "player_data", "kill", "+", 1)
		if es.isbot(userid):
			username = es.getplayername(userid)
			if themap() == "de_inferno_pro":
				if weapon in "scout, awp":
					unlock_check = int(es.keygetvalue(login_id, "player_data", "unlock_4"))
					if not unlock_check:
						unlock_count = keymath(login_id, "player_data", "count_unlock_4", "+", 1)
						if unlock_count >= 1000:
							es.keysetvalue(login_id, "player_data", "unlock_4", 1)
							es.keysetvalue(login_id, "player_data", "count_unlock_4", 0)
							es.server.cmd('es_xsoon r_unlock %s "I am Aim Soldier and a robot!"' %(attacker))
			if themap() == "cs_complex":
				if weapon in "famas, galil, m4a1, ak47, sg552, aug":
					unlock_check = int(es.keygetvalue(login_id, "player_data", "unlock_3"))
					if not unlock_check:
						unlock_count = keymath(login_id, "player_data", "count_unlock_3", "+", 1)
						if unlock_count >= 1000:
							es.keysetvalue(login_id, "player_data", "unlock_3", 1)
							es.keysetvalue(login_id, "player_data", "count_unlock_3", 0)
							es.server.cmd('es_xsoon r_unlock %s "I am Soldier and a robot!"' %(attacker))
			if "[Flaght]" in username:
				if random.randint(1,25) == 9:
					get_item(attacker, "item9", "#85,85,255요정의 찢어진 날개", 1)
			if "[Normal]" in username:
				if random.randint(1,25) == 9:
					get_item(attacker, "item8", "#255,85,85좀비 샘플", 1)
			if "[Shooter]" in username:
				if random.randint(1,25) == 9:
					get_item(attacker, "item4", "#125,125,125부품 Type A", 1)
				if random.randint(1,999) == 9:
					get_item(attacker, "item2", "#255,255,255화이트 버드#0,0,0의 초대장", 1)
				if random.randint(1,999) == 9:
					get_item(attacker, "item7", "#85,85,255페어리 투어 티켓", 1)
			if not "[Normal]" in username:
				if not "[Shooter]" in username and not "[Flaght]" in username:
					es.server.cmd('es_xsexec %s enemydown' %(attacker))
					point = random.randint(3,6)
					if themap() in NORMAL_WORLD: point = point + (int(sv('level')) - 1) * 4
					if themap() in MONSTER_WORLD: point = point + int(sv('level')) * 9
					if themap() in FAIRY_WORLD: point = point + int(sv('level')) * 15
					attackername = es.getplayername(attacker)
					for ab_userid in gethuman():
						if ab_userid == attacker:
							esc.tell(attacker, "#red %s 보스#default를 처치하여#0,0,255 %s 스코어#default를 획득했습니다." %(username, point))
						else:
							esc.tell(ab_userid, "#blue %s 유저#default가#red %s 보스#default를 처치하여#0,0,255 %s 스코어#default를 획득했습니다." %(attackername, username, point))
					est.killadd(attacker, (point - 1))
	if es.isbot(userid):
		if es.getplayerteam(userid) == int(sv('zombieteam')):
			username = es.getplayername(userid)
			if "[Shooter]" in username or "[Normal]" in username or "[Flaght]" in username:
				if int(sv('zombie_count')) > 0:
					svmath("zombie_count", "-", 1)
					gamethread.delayed(1, est.spawn, (userid))
			if es.getplayerteam(attacker) == int(sv('humanteam')):
				attackersteamid = getplayerid(userid)
				if username == "[Magician] White Bird":
					npc_msg("#blue[Magician] White Bird", "히에에에엑! 사람 살려어어! 괴물이다아아!")
					for to_userid in es.getUseridList():
						if not es.isbot(to_userid):
							if es.getplayerteam(to_userid) > 1:
								to_id = getplayerid(to_userid)
								keymath(to_id, "player_data", "xp", "+", 4567)
					get_item(attacker, "item5", "#blue파란색 물약", 1)
					get_item(attacker, "item6", "#purple보라색 물약", 1)
				if username == "[Gunner] 하까나이":
					gamethread.delayed(0.01, es.server.cmd, ('bot_kick "[Gunner] 하까나이"'))
					est.stopsound("#h", "zeisenproject_-1/autosounds/story_sounds/znm.mp3")
					if str(sv('today')) == "day": bgm_loop.start(158, 99999)
					if str(sv('today')) == "night": bgm_loop.start(113, 99999)
					currentmap = themap()
					es.set("mmusic", "zeisenproject_-1/%s/%s.mp3" %(currentmap, sv('today')))
					est.play("#h", sv('mmusic'))
					npc_msg("#255,255,255%s" %(es.getplayername(attacker)), "코노 자코가")
					get_item(attacker, "item3", "#255,0,0몬스터 투어 티켓", 1)
				if username == "[Gunner] Elite Hunter":
					login_id = getplayerid(attacker)
					if int(es.keygetvalue(login_id, "player_data", "unlock_2")) == 0:
						es.keysetvalue(login_id, "player_data", "unlock_2", 1)
						es.server.cmd('r_unlock %s "Fuuuuuuuuuuuuunk"' %(userid))
				for f_userid in es.getUseridList():
					if est.isalive(f_userid):
						if es.getplayerteam(f_userid) == int(sv('zombieteam')):
							if not deleting_bomb(f_userid):
								x,y,z = es.getplayerlocation(userid)
								if random.randint(0,1): x,y,z = es.getplayerlocation(attacker)
								bot_move(f_userid, x, y, z)
				if themap() in NORMAL_WORLD: est.killadd(attacker, (int(sv('level')) - 1))
				if themap() in MONSTER_WORLD: est.killadd(attacker, (int(sv('level')) + 3))
				if themap() in FAIRY_WORLD: est.killadd(attacker, (int(sv('level')) + 1))
				if not es.isbot(attacker): es.keydelete("assist_group_%s" %(userid), es.getplayersteamid(attacker))
				ruru = 0
				kv = keyvalues.getKeyGroup("assist_group_%s" %(userid))
				for ids in kv:
					ruru = 1
				if ruru == 1:
					es.server.cmd('keygroupsort assist_group_%s dmg_health des #numeric' %(userid))
					rank = 1
					kv = keyvalues.getKeyGroup("assist_group_%s" %(userid))
					for ids in kv:
						if rank == 1:
							assister = getuseridfromsteamid(ids)
							if assister:
								rank = 2
								username = es.getplayername(userid)
								assist_give = -1
								level = int(sv('level'))
								if themap() in NORMAL_WORLD: 
									assist_give = assist_give - (level - 1)
									if not "[Normal]" in username: assist_give = -6
								if themap() in MONSTER_WORLD: 
									assist_give = assist_give - (level + 2)
									if not "[Shooter]" in username: assist_give = -20
								if themap() in FAIRY_WORLD: 
									assist_give = 1
									if not "[Flaght]" in username: assist_give = -30
								est.deathadd(assister, assist_give)
								esc.tell(assister, "#red %s 좀비#255,255,255를 어시스트 했습니다!" %(username))

def getuseridfromsteamid(steamid):
	for userid in es.getUseridList():
		_steamid = es.getplayersteamid(userid)
		if _steamid == str(steamid):
			return userid
	return 0

def bomb_planted(ev):
	userid = int(ev['userid'])
	x,y,z = es.getplayerlocation(userid)
	es.set("c4_x", x)
	es.set("c4_y", y)
	es.set("c4_z", z)
	est.cash(userid, "+", 1000)

def bomb_exploded(ev):
	userid = int(ev['userid'])
	est.cash(userid, "+", 3000)

def player_spawn(ev):
	userid = int(ev['userid'])
	userteam = es.getplayerteam(userid)
	steamid = es.getplayersteamid(userid)
	if userteam > 1:
		if steamid != "BOT":
			es.setplayerprop(userid, "CCSPlayer.baseclass.localdata.m_Local.m_iHideHUD", 8)
			est.setplayercolor(userid, 255, 255, 255, 255, 0)
			if themap() in str(REST_MAPS): es.setplayerprop(userid, _blockprop, 5)
			if not themap() in str(REST_MAPS): es.setplayerprop(userid, _blockprop, 2)
			login_id = getplayerid(userid)
			if int(sv('fight')) == 0:
				x,y,z = es.getplayerlocation(userid)
				es.set("spawn_x", x)
				es.set("spawn_y", y)
				es.set("spawn_z", z)
			username = es.getplayername(userid)
			fm = "%s " %(username)
			es.keysetvalue(login_id, "player_data", "username", fm)
			if themap() in str(REST_MAPS):
				if int(es.keygetvalue(login_id, "player_data", "item1")) > 0:
					est.setmodel(userid, "player/ct_sas")
			if login_id in str(sv('support_ranker')):
				if str(es.keygetvalue(login_id, "player_data", "fire_count")) != "0":
					est.setmodel(userid, es.keygetvalue(login_id, "player_data", "fire_count"))
			health = int(es.keygetvalue(login_id, "player_data", "health"))
			speed = float(es.keygetvalue(login_id, "player_data", "speed")) / 1000
			mp = int(es.keygetvalue(login_id, "player_data", "mp"))
			mastery = str(es.keygetvalue(login_id, "player_data", "mastery"))
			#es.dbgmsg(0, mastery)
			if "스칼렛" in mastery:
				health += 4444
				esc.msg("#0,0,0[어빌리티]#0,255,255 %s 유저#255,255,255는#255,255,0 %s효과로 체력 4444 지급!" %(username, mastery))
			if "흡혈귀" in mastery:
				health += 650
				esc.msg("#0,0,0[어빌리티]#0,255,255 %s 유저#255,255,255는#255,255,0 %s효과로 체력 650 지급!" %(username, mastery))
			if "봄버맨" in mastery:
				est.give(userid, "weapon_hegrenade")
				est.setammo(userid, "weapon_hegrenade", 99)
				esc.msg("#0,0,0[어빌리티]#0,255,255 %s 유저#255,255,255는#255,255,0 %s효과로 수류탄 99개 지급!" %(username, mastery))
			if "용병(AR)" in mastery:
				esc.msg("#0,0,0[어빌리티]#0,255,255 %s 유저#255,255,255는#255,255,0 %s효과로 AR 데미지 50％ 상승!" %(username, mastery))
			if "용병(SR)" in mastery:
				esc.msg("#0,0,0[어빌리티]#0,255,255 %s 유저#255,255,255는#255,255,0 %s효과로 무기 변경 속도 50％ 상승!" %(username, mastery))
			if "아이언 맨" in mastery:
				IRON_MAN[userid] = 2
				IRON_MAN_PRESS_1[userid] = 0
				IRON_MAN_PRESS_2[userid] = 0
				est.give(userid, "item_assaultsuit")
				gamethread.delayed(0.1, est.setarmor, (userid, 5100))
				esc.msg("#0,0,0[어빌리티]#0,255,255 %s 유저#255,255,255는#255,255,0 %s효과로 방탄복 5000 상승!" %(username, mastery))
			skill = int(es.keygetvalue(login_id, "player_data", "skill1"))
			if skill:
				health = health + (skill * 15)
			es.setplayerprop(userid, _healthprop, health)
			es.setplayerprop(userid, _speedprop, speed)
			current_mp[userid] = mp
			one_damage_reset(userid)
			one_damage_armor_reset(userid)
			if themap() == "de_nightfever":
				es.server.cmd('es_xfire %s env_soundscape Disable' %(userid))
				es.server.cmd('es_xfire %s env_soundscape_proxy Disable' %(userid))
				if str(sv('sv_password')) != "nipperkk":
					esc.tell(userid, "#255,255,255＊ 이 곳은 황혼주점입니다. NPC와 대화/거래 등이 가능한 곳입니다.")
					esc.tell(userid, "#255,255,255＊ 낮 / #125,125,125밤 #255,255,255이냐에 따라 NPC의 출현이 달라집니다.")
					esc.tell(userid, "#255,255,255＊ 나가는 방법은 텔레포트 NPC인 소닉에게 찾아가보세요.")
				else:
					es.setpos(userid, -1300, 1545, 75)
					es.setplayerprop(userid, _blockprop, 2)
				est.removeidle("weapon")
				if int(sv('bot_quota')) > 2:
					est.give(userid, "weapon_p90")
				else:
					if str(sv('sv_password')) == "":
						if steamid == "STEAM_0:1:17803258":
							if random.randint(1,2) == 1: es.setpos(userid, 934, 1263, 60)
		if steamid == "BOT":
			es.setplayerprop(userid, _blockprop, 17)
			username = es.getplayername(userid)
			username_args = username.split()
			#########################################
			#BOT Name Type : [Show Ability] Username#
			#########################################

			if not "[Human]" in username and not "[Extra]" in username:
				if userteam == int(sv('humanteam')):
					zombieteam = int(sv('zombieteam'))
					es.changeteam(userid, zombieteam)
				if userteam == int(sv('zombieteam')):
					es.keygroupdelete("assist_group_%s" %(userid))
					if int(sv('round')) != 8: es.keygroupcreate("assist_group_%s" %(userid))
					if int(sv('fight')) == 0:
						if themap() == "cs_assault2_goban_b3": es.setpos(userid, 142, 2132, 318)
					variable_level = int(sv('level'))
					
					if int(sv('fight')) == 1:
						if es.getplayerteam(userid) == 2:
							rand_list = []
							for index in es.getEntityIndexes("info_player_counterterrorist"):
								rand_list.append(index)
							select_index = random.choice(rand_list)
							loc = es.getindexprop(select_index, "CBaseEntity.m_vecOrigin")
							loc_arg = loc.split(",") 
							es.setpos(userid, loc_arg[0], loc_arg[1], loc_arg[2])
						if es.getplayerteam(userid) == 3:
							rand_list = []
							for index in es.getEntityIndexes("info_player_terrorist"):
								rand_list.append(index)
							select_index = random.choice(rand_list)
							loc = es.getindexprop(select_index, "CBaseEntity.m_vecOrigin")
							loc_arg = loc.split(",") 
							es.setpos(userid, loc_arg[0], loc_arg[1], loc_arg[2])

					if int(es.getentityindex("planted_c4")) > 0:
						c4_index = es.getentityindex("planted_c4")
						bot_move(userid, sv('c4_x'), sv('c4_y'), sv('c4_z'))

					if not "[Normal]" in username:
						if username == "[Magician] White Bird":
							est.sethealth(userid, 1000)
							est.setarmor(userid, 123456)
							est.speed(userid, 1.4)
							es.set("magician_id", userid)
						if username == "[Gunner] 하까나이":
							est.teleport(userid, -1032, 497, 80)
							est.sethealth(userid, 100)
							player_count = getplayercount()
							if player_count == 1: est.setarmor(userid, 999)
							if player_count >= 2: est.setarmor(userid, 99999)
							est.give(userid, "weapon_ak47")
							est.setplayercolor(userid, 255, 125, 0, 255)
							es.server.cmd('es_xdelayed 0.1 r_setmodel %s "models/props/cs_havana/gazebo.mdl"' %(userid))
						if username == "[Unknown] .":
							est.teleport(userid, 999, 999, 99999)
							es.changeteam(userid, 1)
							es.set("m1_id", userid)
							es.server.cmd('es_xfire %s soundent Disable' %(userid))
							es.server.cmd('es_xfire %s env_soundscape Disable' %(userid))
							es.server.cmd('es_xfire %s env_soundscape_proxy Disable' %(userid))
						if username == "[Unknown] ?":
							est.teleport(userid, 999, 999, 99999)
							es.server.cmd('es_xfire %s env_soundscape Disable' %(userid))
							es.server.cmd('es_xfire %s env_soundscape_proxy Disable' %(userid))
						if username == "[Unknown] Crizi":
							est.hookkey(userid, "speed")
							est.give(userid, "weapon_m4a1")
							est.god(userid, 1)
							est.setmodel(userid, "player/pil/fast_v5/pil_fast_v5.mdl")
							est.setplayercolor(userid, 0, 0, 0, 200, 1)
							es.set("crizi_id", userid)
						if username == "[Reckless] Fade":
							set_model(userid, "player/slow/fallout_3/glowing_one/slow.mdl")
							es.setplayerprop(userid, _speedprop, 1)
							es.setplayerprop(userid, _healthprop, 10000)
							boss_skill("#blue[Reckless] Fade", "#125,255,125첫번째 탄생")
							est.killset(userid, 100)
							es.server.cmd('es_xgive %s weapon_knife' %(userid))
							es.server.cmd('es_xdelayed 1 es_xsexec %s use weapon_knife' %(userid))
						if "[Flaght]" in username:
							est.removeweapon(userid, 1)
							est.removeweapon(userid, 2)
							est.removeweapon(userid, 3)
							if variable_level == 1: giveweapon = random.choice(["deagle", "p228", "glock", "usp", "elite"])
							if variable_level == 2: giveweapon = random.choice(["tmp", "mac10", "ump45", "mp5navy"])
							if variable_level == 3: giveweapon = random.choice(["p90", "galil", "famas"])
							if variable_level >= 4: giveweapon = random.choice(["m4a1", "ak47", "sg552", "aug"])
							es.server.cmd('es_xsoon es_xgive %s weapon_%s' %(userid, giveweapon))
						if "[Shooter]" in username:
							set_model(userid, "player/slow/me2/geth_trooper/slow.mdl")
							est.removeweapon(userid, 1)
							est.removeweapon(userid, 2)
							est.removeweapon(userid, 3)
							if variable_level == 1: giveweapon = random.choice(["deagle", "p228", "glock", "usp", "elite"])
							if variable_level == 2: giveweapon = random.choice(["tmp", "mac10", "ump45", "mp5navy"])
							if variable_level == 3: giveweapon = random.choice(["p90", "galil", "famas"])
							if variable_level >= 4: giveweapon = random.choice(["m4a1", "ak47", "sg552", "aug"])
							es.server.cmd('es_xsoon es_xgive %s weapon_%s' %(userid, giveweapon))
						if username == "[Gunner] Elite Sniper":
							set_model(userid, "player/slow/eve/slow.mdl")
							es.setplayerprop(userid, _speedprop, 1.5)
							es.setplayerprop(userid, _healthprop, 250)
							es.server.cmd("es_xgive %s item_assaultsuit" %(userid))
							est.killset(userid, 100)
							est.removeweapon(userid, 1)
							est.removeweapon(userid, 2)
							est.removeweapon(userid, 3)
							est.give(userid, "weapon_awp")
						if username == "[Gunner] The Sea":
							set_model(userid, "player/slow/eve/slow.mdl")
							est.setplayercolor(userid, 85, 85, 255, 255)
							es.setplayerprop(userid, _speedprop, 1.55)
							es.setplayerprop(userid, _healthprop, 550)
							es.server.cmd("es_xgive %s item_assaultsuit" %(userid))
							est.killset(userid, 550)
							est.removeweapon(userid, 1)
							est.removeweapon(userid, 2)
							est.removeweapon(userid, 3)
							est.give(userid, "weapon_sg550")
						if username == "[Gunner] Slayer":
							set_model(userid, "player/slow/fallout_3/glowing_one/slow.mdl")
							es.setplayerprop(userid, _speedprop, 1.5)
							es.setplayerprop(userid, _healthprop, 400)
							est.killset(userid, 300)
							est.removeweapon(userid, 1)
							est.removeweapon(userid, 2)
							est.removeweapon(userid, 3)
							est.give(userid, "weapon_tmp")
						if username == "[Gunner] Roca":
							set_model(userid, "player/slow/fallout_3/glowing_one/slow.mdl")
							es.setplayerprop(userid, _speedprop, 1.5)
							es.setplayerprop(userid, _healthprop, 250)
							est.killset(userid, 100)
							est.removeweapon(userid, 1)
							est.removeweapon(userid, 2)
							est.removeweapon(userid, 3)
							est.give(userid, "weapon_m4a1")
						if username == "[Gunner] Elite Hunter":
							set_model(userid, "player/slow/section_8/slow.mdl")
							es.setplayerprop(userid, _speedprop, 1.5)
							es.setplayerprop(userid, _healthprop, 999)
							es.server.cmd("es_xgive %s item_assaultsuit" %(userid))
							est.killset(userid, 444)
							est.removeweapon(userid, 1)
							est.removeweapon(userid, 2)
							est.removeweapon(userid, 3)
							est.give(userid, "weapon_ak47")
						if username == "[Bomber] ^^":
							est.setmodel(userid, "models/player/slow/fallout_3/ghoul/slow.mdl")
							est.setplayercolor(userid, 255, 125, 125, 255, 1)
							es.setplayerprop(userid, _speedprop, 1.5)
							es.setplayerprop(userid, _healthprop, 2500)
							est.killset(userid, 100)
							est.removeweapon(userid, 1)
							est.removeweapon(userid, 2)
							est.give(userid, "weapon_hegrenade")
						if username == "[Gunner] Elite Killer":
							set_model(userid, "player/slow/section_8/slow.mdl")
							es.setplayerprop(userid, _speedprop, 1.5)
							es.setplayerprop(userid, _healthprop, 150)
							est.setplayercolor(userid, 0, 0, 0, 255)
							est.killset(userid, 100)
							est.removeweapon(userid, 1)
							est.removeweapon(userid, 2)
							est.removeweapon(userid, 3)
							est.give(userid, "weapon_aug")
						if username == "[Gunner] Camp Killer":
							if "cs_" in themap():
								es.server.cmd('bot_kick "%s"' %(username))
								return
							if themap() == "de_aztec":
								es.setpos(userid, -2966, 724, -64)
							es.setplayerprop(userid, _healthprop, 9999999)
							est.setmodel(userid, "player/slow/me2/geth_trooper/slow.mdl")
							es.setplayerprop(userid, _speedprop, 0)
							est.setplayercolor(userid, 0, 0, 0, 255, 0)
							es.server.cmd("es_xgive %s item_assaultsuit" %(userid))
							est.killset(userid, 50)
							est.removeweapon(userid, 1)
							est.removeweapon(userid, 2)
							est.removeweapon(userid, 3)
							es.server.cmd('es_xsoon es_xgive %s weapon_mp5navy' %(userid))
						if username == "[Gunner] Elite Shooter":
							set_model(userid, "player/slow/me2/geth_trooper/slow.mdl")
							es.setplayerprop(userid, _speedprop, 1.25)
							est.killset(userid, 50)
							est.removeweapon(userid, 1)
							est.removeweapon(userid, 2)
							est.removeweapon(userid, 3)
							if variable_level == 1: giveweapon = random.choice(["deagle", "p228", "glock", "usp", "elite"])
							if variable_level == 2: giveweapon = random.choice(["glock", "tmp", "mac10", "ump45", "mp5navy"])
							if variable_level == 3: giveweapon = random.choice(["glock", "p90", "galil", "famas"])
							if variable_level >= 4: giveweapon = random.choice(["glock", "m4a1", "ak47", "sg552", "aug"])
							es.server.cmd('es_xsoon es_xgive %s weapon_%s' %(userid, giveweapon))
						if username == "[Rage] Ivas":
							set_model(userid, "player/slow/eve/slow.mdl")
							est.setplayercolor(userid, 255, 255, 255, 255, 0)
							est.setarmor(userid, (100 + variable_level * 250))
							es.setplayerprop(userid, _healthprop, (5123 + variable_level * 1513))
							default_speed = (1 + variable_level * 0.03)
							es.setplayerprop(userid, _speedprop, default_speed)
							est.killset(userid, 50)
							est.setplayercolor(userid, 255, 255, 255, 255, 0)
						if username == "[Bulldozer] Templer":
							set_model(userid, "player/slow/berserkerin/slow_big.mdl")
							est.setarmor(userid, (100 + variable_level * 500))
							es.setplayerprop(userid, _healthprop, (5183 + variable_level * 1329))
							es.setplayerprop(userid, _speedprop, (0.96 + variable_level * 0.04))
							#es.remove("hat_%s" %(userid))
							#givehat(userid, 255, 255, 255, 255) #complete - player_death
							est.killset(userid, 50)
					else:
						number = int(username_args[1])
						health = int(es.getplayerprop(userid, _healthprop))
						health += number
						health = health + (112 + 204 * variable_level)
						es.setplayerprop(userid, _healthprop, health)
						es.setplayerprop(userid, _speedprop, (0.98 + variable_level * 0.02))
						model_able = random.choice(["models/player/slow/berserkerin/slow.mdl", "models/player/techknow/hellknight/hellknight.mdl"])
						es.server.cmd('es_xdelayed 0.1 r_setmodel %s "%s"' %(userid, model_able))
						est.setarmor(userid, (100 + variable_level * 50))
			else:
				if userteam == int(sv('zombieteam')):
					es.changeteam(userid, sv('humanteam'))
				else:
					est.killset(userid, 0)
					est.deathset(userid, 0)
					if "[Human]" in username:
						top_damage[userid] = 0
						est.removeweapon(userid, 1)
						est.removeweapon(userid, 2)
						est.removeweapon(userid, 3)
						if userteam == 2: est.setplayercolor(userid, 255, 155, 0, 255)
						if userteam == 3: est.setplayercolor(userid, 105, 105, 255, 255)
						if int(sv('round')) == 1:
							if userteam == 2: est.give(userid, "weapon_elite")
							if userteam == 3: est.give(userid, "weapon_deagle")
						else:
							if userteam == 2: est.give(userid, "weapon_galil")
							if userteam == 3: est.give(userid, "weapon_m4a1")
					if username == "[Extra] 오오타 준페이":
						es.setplayerprop(userid, _healthprop, 999)
						est.removeweapon(userid, 1)
						est.removeweapon(userid, 2)
						est.removeweapon(userid, 3)
						es.server.cmd('es_xdelayed 0.2 r_setmodel %s "models/player/techknow/paranoya/paranoya.mdl"' %(userid))
						if int(sv('round')) == 1:
							es.server.cmd('es_xgive %s weapon_p228' %(userid))
						else:
							es.server.cmd('es_xgive %s weapon_famas' %(userid))
		A = int(es.getplayerprop(userid, _healthprop))
		max_health[userid] = A

########################################################################################### Block Fuctions

def set_model(userid, model):
	model = model.replace("\\", "/")
	if not model.startswith("models/"):
		model = "models/%s" % model
	if not model.endswith(".mdl"):
		model += ".mdl"
	es.server.cmd('es_xdelayed 0.1 r_setmodel %s "%s"' %(userid, model))

def test99():
	#for a_userid in es.getUseridList():
	#	if es.isbot(a_userid):
	#		spe.call("Follow", spe.getPlayer(a_userid), spe.getPlayer(4))
	get_item(sv('give_userid'), "item2", "#gold노말 투어 티켓", 1)

def test9():
	#for a_userid in es.getUseridList():
	#	if es.isbot(a_userid):
	#		spe.call("Follow", spe.getPlayer(a_userid), spe.getPlayer(4))
	get_item(sv('give_userid'), "item3", "#gold몬스터 투어 티켓", 1)

def get_item(userid, key, real, much):
	steamid = getplayerid(userid)
	username = es.getplayername(userid)
	keymath(steamid, "player_data", key, "+", much)
	esc.msg("#255,255,255＠#blue %s 유저#255,255,255님이 %s 아이템#255,255,255을 %s개 획득했습니다." %(username, real, much))

def update_key():
	kv = keyvalues.getKeyGroup("")
	for steamid in kv:
		es.keysetvalue("total_players", steamid, "volume", 1.0)

def gethuman():
    return (userid for userid in es.getUseridList() if es.getplayersteamid(userid) != 'BOT')
 
def getbot(): 
    return (userid for userid in es.getUseridList() if es.getplayersteamid(userid) == 'BOT') 

def getalivehuman():
    return (userid for userid in es.getUseridList() if es.getplayersteamid(userid) != 'BOT' and not isdead(userid))
 
def getalivebot(): 
    return (userid for userid in es.getUseridList() if es.getplayersteamid(userid) == 'BOT' and not isdead(userid)) 

def player_blind(ev):
	userid = int(ev['userid'])
	if not es.isbot(userid):
		if float(es.getplayerprop(userid, "CCSPlayer.m_flFlashMaxAlpha")) > 230:
			es.setplayerprop(userid, "CCSPlayer.m_flFlashMaxAlpha", 230)
def timerz_command():
	currentmap = themap()
	if int(sv('black_fade')) == 1:
		est.fade("#h", 0, 1, 1.2, 0, 0, 0, 255)
	if getplayercount() == 0:
		if str(sv('sv_password')) == "nipperkk":
			es.server.cmd('changelevel de_nightfever')
	if int(sv('allfade')) == 1:
		for userid in es.getUseridList():
			est.fade(userid, 0, 0.15, 1.15, 0, 0, 0, 255)
	if themap() == "de_colors":
		userid = int(sv('magician_id'))
		if userid:
			if est.getarmor(userid) < 123456:
				climax = 30
				if est.getarmor(userid) <= 30000: climax = 3
				if random.randint(1,climax) == 1:
					for to_userid in getalivehuman():
						usermsg.hudhint(to_userid, "당신들을 위한 특별 선물입니다!")
						xxx,yyy,zzz = es.getplayerlocation(to_userid)
						est.makeentity('prop_physics', 'props_c17/oildrum001_explosive', xxx, yyy, zzz)
						est.makeentity('prop_physics', 'props_c17/oildrum001_explosive', xxx, yyy, zzz)
						est.makeentity('prop_physics', 'props_c17/oildrum001_explosive', xxx, yyy, zzz)
						est.makeentity('prop_physics', 'props_c17/oildrum001_explosive', xxx, yyy, zzz)
						est.makeentity('prop_physics', 'props_c17/oildrum001_explosive', xxx, yyy, zzz)
						est.makeentity('prop_physics', 'props_c17/oildrum001_explosive', xxx, yyy, zzz)
						est.makeentity('prop_physics', 'props_c17/oildrum001_explosive', xxx, yyy, zzz)
						est.makeentity('prop_physics', 'props_c17/oildrum001_explosive', xxx, yyy, zzz)
						xxx,yyy,zzz = es.getplayerlocation(userid)
						est.makeentity('prop_physics', 'props_c17/oildrum001_explosive', xxx, yyy, zzz)
						for index in es.getEntityIndexes("prop_physics"):
							es.setindexprop(index, "CPhysicsProp.baseclass.baseclass.m_flModelScale", float(random.randint(10,250))/ 100)
							es.setindexprop(index, "CPhysicsProp.baseclass.baseclass.baseclass.m_hOwnerEntity", es.getplayerhandle(userid))
						es.server.cmd('es_xdelayed 5 es_xfire %s prop_physics break' %(userid))
				if random.randint(1,100) == 45:
					for to_userid in gethuman():
						usermsg.hudhint(to_userid, "자아아아아! 전부 위로 위로!")
						est.physpush(to_userid, 0, 0, 300)
						gamethread.delayed(0.3, est.physpush, (to_userid, 0, 0, 300))
						gamethread.delayed(0.6, est.physpush, (to_userid, 0, 0, 300))
						gamethread.delayed(0.9, est.physpush, (to_userid, 0, 0, 300))
						gamethread.delayed(1.2, est.physpush, (to_userid, 0, 0, 300))
						gamethread.delayed(1.5, est.physpush, (to_userid, 0, 0, 300))
				if random.randint(1,250) == 45:
					for to_userid in gethuman():
						usermsg.hudhint(to_userid, "뒤죽박죽! ")
						est.physpush(to_userid, 300, 0, 0)
						gamethread.delayed(0.3, est.physpush, (to_userid, 0, 0, 300))
						gamethread.delayed(0.6, est.physpush, (to_userid, 0, 3000, 0))
						gamethread.delayed(0.9, est.physpush, (to_userid, 0, 0, 300))
						gamethread.delayed(1.2, est.physpush, (to_userid, 300, 0, 300))
						gamethread.delayed(1.5, est.physpush, (to_userid, 3000, 300, 300))
	for userid in gethuman():
		if es.getplayerteam(userid) > 1:
			login_id = getplayerid(userid)
			level = es.keygetvalue(login_id, "player_data", "level")
			if not level: continue
			xp = int(es.keygetvalue(login_id, "player_data", "xp"))
			nextxp = int(es.keygetvalue(login_id, "player_data", "nextxp"))
			level = int(es.keygetvalue(login_id, "player_data", "level"))
			health = int(es.keygetvalue(login_id, "player_data", "skillpoint"))
			speed = int(es.keygetvalue(login_id, "player_data", "stetpoint"))
			bp = int(es.keygetvalue(login_id, "player_data", "bp"))
			mp = current_mp[userid]
			money = int(es.keygetvalue(login_id, "player_data", "money"))
			human_xp = int(es.keygetvalue(login_id, "player_data", "human_xp"))
			mg = ""
			if est.isalive(userid):
				mastery = str(es.keygetvalue(login_id, "player_data", "mastery"))
				if mastery == "아이언 맨 ":
					if IRON_MAN[userid] == 2: usermsg.hudmsg(userid, "Press Left Mouse", 999, 0.3, 0.3)
					if IRON_MAN[userid] == 3: usermsg.hudmsg(userid, "Press Right Mouse", 999, 0.3, 0.3)
				me_health = est.gethealth(userid)
				me_armor = est.getarmor(userid)
				me_cash = es.getplayerprop(userid, _moneyprop)
				me_gun = est.getgun(userid)
				if not "none" in me_gun:
					r,g,b,a = getentitycolor(est.getweaponindex(userid, me_gun))
				me_clip = est.getclipammo(userid, me_gun)
				me_ammo = est.getammo(userid, me_gun)
				usermsg.hudmsg(userid, "HP %s│AP %s" %(me_health, me_armor), 0, 0.02, 0.93, r1=0)
				usermsg.hudmsg(userid, "%s Cash\n%s/%s" %(me_cash, me_clip, me_ammo), 1, 0.9, 0.93, r1=r, g1=g, b1=b)
				est.cashadd(userid, es.keygetvalue(login_id, "player_data", "mp"))
				burn_times = int(burn_time[userid])
				if burn_times > 0:
					burn_times -= 1
					burn_time[userid] = burn_times
					est.burn(userid, 1)
			if not themap() in str(REST_MAPS):
				keymath(login_id, "player_data", "play_time", "+", 1)
				if int(es.keygetvalue(login_id, "player_data", "supporter_time")) > 0: keymath(login_id, "player_data", "supporter_time", "-", 1)
			if int(es.keygetvalue(login_id, "player_data", "supporter_time")) > 0:
				spt = int(es.keygetvalue(login_id, "player_data", "supporter_time"))
				spt_min = spt / 60
				spt_min = est.rounddecimal(spt_min, 0)
				spt_min = spt_min.replace(".0", "")
				spt_sec = spt % 60
				spt_hour = int(spt_min) / 60
				spt_hour = est.rounddecimal(spt_hour, 0)
				spt_hour = spt_hour.replace(".0", "")
				if int(spt_hour) != 0:
					spt_min = int(spt_min) - (int(spt_hour) * 60)
				spt_day = int(spt_hour) / 24
				spt_day = est.rounddecimal(spt_day, 0)
				spt_day = spt_day.replace(".0", "")
				if int(spt_day) != 0:
					spt_hour = int(spt_hour) - (int(spt_day) * 24)
				mg = "\n \nSupporter Time : %s일 %s시 %s분 %s초" %(spt_day, spt_hour, spt_min, spt_sec)
				mg_args = mg.split()
				if mg_args[3] == "0일": mg = mg.replace("0일 ", "")
				if mg_args[4] == "0시": mg = mg.replace("0시 ", "")
				if mg_args[5] == "0분": mg = mg.replace("0분 ", "")
				if mg_args[6] == "0초": mg = mg.replace(" 0초", "")
			usermsg.keyhint(userid, "Level : %s(%s/%s Xp)\n \nSkill Point : %s │ Stat Point : %s\n현재 MP : %s │ BP : %s │ 인기도 : %s\nMoney : %s엔%s" %(level, xp, nextxp, health, speed, mp, bp, human_xp, money, mg))
			if xp >= nextxp:
				xp = keymath(login_id, "player_data", "xp", "-", nextxp)
				nextxp = keymath(login_id, "player_data", "nextxp", "+", 10)
				level = keymath(login_id, "player_data", "level", "+", 1)
				skillpoint = keymath(login_id, "player_data", "skillpoint", "+", 1)
				stetpoint = keymath(login_id, "player_data", "stetpoint", "+", 1)
				un = es.getplayername(userid)
				esc.msg("#blue %s 유저#255,255,255의 레벨이 상승했습니다. #0,255,0(%s → %s)" %(un, level - 1, level))
	if not currentmap in REST_MAPS:
		if not currentmap in SPECIAL_MAPS:
			if currentmap in MONSTER_WORLD:
				if int(sv('bot_quota')) == 1:
					es.server.cmd('bot_add "[Gunner] Elite Killer"')
					es.set("round", 1)
					es.server.cmd('mp_freezetime 0')
					if int(sv('level')) >= 6: es.set("level", 5)
			if currentmap in str(FAIRY_WORLD):
				if int(sv('bot_quota')) == 1:
					es.server.cmd('bot_add "[Gunner] Slayer"')
					es.set("round", 1)
					es.server.cmd('mp_freezetime 0')
					if int(sv('level')) >= 6: es.set("level", 5)
			if currentmap in NORMAL_WORLD:
				if int(sv('bot_quota')) == 1:
					es.server.cmd('bot_add "[Gunner] Elite Shooter"')
					es.set("round", 1)
					es.server.cmd('mp_freezetime 0')
					if int(sv('level')) >= 6: es.set("level", 5)
		else:
			if currentmap == "de_colors":
				if int(sv('bot_quota')) == 1:
					es.server.cmd('bot_add "[Magician] White Bird"')
					es.set("round", 1)
					es.server.cmd('mp_freezetime 0')
					if int(sv('level')) >= 6: es.set("level", 5)
			if currentmap == "de_train":
				if int(sv('bot_quota')) == 1:
					es.server.cmd('bot_add "[Reckless] Fade"')
					es.set("round", 1)
					es.server.cmd('mp_freezetime 0')
					if int(sv('level')) >= 6: es.set("level", 5)
	else:
		if int(sv('say_block')) == 0:
			if str(sv('sv_password')) != "nipperkk" and themap() == "de_nightfever":
				if int(sv('player_count')) == 1:
					server_hour_time = int(time.strftime('%H'))
					for userid in es.getUseridList():
						if es.getplayerteam(userid) > 1: 
							tuserid = userid
					login_id = getplayerid(tuserid)
					if str(es.keygetvalue(login_id, "player_data", "mastery")) == "없음 ":
						if int(es.keygetvalue(login_id, "player_data", "stetpoint")) == int(es.keygetvalue(login_id, "player_data", "level")):
							if server_hour_time == 24 or server_hour_time <= 3:
								if random.randint(4,444) == 4:
									es.server.cmd('sv_password nipperkk')
									bgm_loop.stop()
									nightfever_dead()
									est.stopsound("#h", "zeisenproject_-1/de_nightfever/%s.mp3" %(sv('today')))
									es.set("allfade", 1)
									npc_msg("#255,0,0???", "아무도 없나보네요...")
									gamethread.delayed(4, npc_msg, ("#255,0,0???", "당신, 저랑 놀지 않으실래요?"))
									gamethread.delayed(4, vampire_select_.send, (tuserid))
		if str(sv('sv_password')) == "nipperkk":
			for_timer = int(sv('for_timer')) + 1
			es.set("for_timer", for_timer)
			if for_timer == 3:
				es.set("for_timer", 0)
				for_timer = 0
				getu = int(sv('crizi_id'))
				if getu > 0:
					es.emitsound("player", getu, "zeisenproject_-1/autosounds/story_sounds/crizi_idle.mp3", 1.0, 1.0)
					es.emitsound("player", getu, "zeisenproject_-1/autosounds/story_sounds/crizi_idle.mp3", 1.0, 1.0)
					es.emitsound("player", getu, "zeisenproject_-1/autosounds/story_sounds/crizi_idle.mp3", 1.0, 1.0)
					es.emitsound("player", getu, "zeisenproject_-1/autosounds/story_sounds/crizi_idle.mp3", 1.0, 1.0)
					es.emitsound("player", getu, "zeisenproject_-1/autosounds/story_sounds/crizi_idle.mp3", 1.0, 1.0)
			if int(sv('teleport_timer')) > 0:
				teleport_timer = svmath("teleport_timer", "-", 1)
				if teleport_timer == 0: es.server.cmd('sm_map %s' %(sv('will_map')))
		if random.randint(1,100) == 77:
			if israining(): thunder()
	for userid in es.getUseridList():
                if not es.isbot(userid): continue
		if themap() == "cs_complex":
			x,y,z = es.getplayerlocation(userid)
			if z <= float(-300):
				es.setpos(userid, -278, -1118, 41)
		check_username = es.getplayername(userid)
		if "[Bomber]" in check_username:
			if es.isbot(userid) and est.isalive(userid):
				first_check = est.getweaponindex(userid, "weapon_flashbang")
				if first_check > 0:
					weapon_name = es.entitygetvalue(first_check, "classname")
					es.server.cmd('es_xsexec %s use "%s"' %(userid, weapon_name))
				else:
					first_check = est.getweaponindex(userid, "weapon_hegrenade")
					if first_check > 0:
						weapon_name = es.entitygetvalue(first_check, "classname")
						es.server.cmd('es_xsexec %s use "%s"' %(userid, weapon_name))
		if "[Gunner]" in check_username or "[Shooter]" in check_username or "[Flaght]" in check_username:
			if es.isbot(userid) and est.isalive(userid):
				if est.getgun(userid) != "weapon_c4":
					est.removeweapon(userid, 3)
					first_check = est.getweaponindex(userid, 1)
					if first_check > 0:
						weapon_name = es.entitygetvalue(first_check, "classname")
						es.server.cmd('es_xsexec %s use "%s"' %(userid, weapon_name))
					else:
						first_check = est.getweaponindex(userid, 2)
						if first_check > 0:
							weapon_name = es.entitygetvalue(first_check, "classname")
							es.server.cmd('es_xsexec %s use "%s"' %(userid, weapon_name))
		for username in WEAPON_BOT:
			if username == check_username:
				if es.isbot(userid) and est.isalive(userid):
					if est.getgun(userid) != "weapon_c4":
						est.removeweapon(userid, 3)
						first_check = est.getweaponindex(userid, 1)
						if first_check > 0:
							weapon_name = es.entitygetvalue(first_check, "classname")
							es.server.cmd('es_xsexec %s use "%s"' %(userid, weapon_name))
						else:
							first_check = est.getweaponindex(userid, 2)
							if first_check > 0:
								weapon_name = es.entitygetvalue(first_check, "classname")
								es.server.cmd('es_xsexec %s use "%s"' %(userid, weapon_name))

def vampire_select(userid, choice, popupname):
	steamid = getplayerid(userid)
	if popupname == "vampire_select_1":
		if not str(choice) in "1, 2":
			esc.tell(userid, "#255,255,255어떻게 하지...")
		else:
			if str(choice) == "1":
				npc_msg("#255,0,0???", "이렇게 쉽게 넘어오다니...")
				gamethread.delayed(4, npc_msg, ("#255,0,0???", "이런 사람은.. #255,0,0필요 없어요."))
				gamethread.delayed(4.5, est.slay, (userid))
			if str(choice) == "2":
				if str(sv('today')) == "day": today_prefix = "아침"
				if str(sv('today')) == "night": today_prefix = "밤"
				npc_msg("#255,0,0???", "왜... 거부하는거죠? 느긋한 %s에.. 아무도 없잖아요. 좋지 않은가요?" %(today_prefix))
				gamethread.delayed(4, npc_msg, ("#255,0,0???", "다시 한번 생각해봐요..."))
				gamethread.delayed(4, vampire_select_2.send, (userid))
	if popupname == "vampire_select_2":
		if not str(choice) in "1, 2":
			esc.tell(userid, "#255,255,255어떻게 하지...")
		else:
			if str(choice) == "1":
				npc_msg("#255,0,0???", "역시♪ 내가 보는 눈은 있다니까.")
				gamethread.delayed(4.5, npc_msg, ("#255,0,0???", "좋아요... 아무도 없는데... #255,0,0즐겨야죠."))
				gamethread.delayed(4.5, es.keysetvalue, (steamid, "player_data", "mastery", "흡혈귀 "))
				gamethread.delayed(4.5, es.keygroupsave, (steamid, "|bot/player_data"))
				gamethread.delayed(5, est.slay, (userid))
			if str(choice) == "2":
				npc_msg("#255,0,0???", "그런가요...")
				gamethread.delayed(4, npc_msg, ("#255,0,0???", "이런 사람은.. #255,0,0필요 없어요."))
				gamethread.delayed(4.5, est.slay, (userid))
		
def reset_player(login_id):
	test = 1
	if test == 1:
		if test == 1:
			if test == 1:
				if test == 1:
					if test == 1:
						if test == 1:
							es.keygroupcreate(login_id)
							es.keycreate(login_id, "player_data")
							es.keysetvalue(login_id, "player_data", "level", 1)
							es.keysetvalue(login_id, "player_data", "xp", 0)
							es.keysetvalue(login_id, "player_data", "nextxp", 10)
							es.keysetvalue(login_id, "player_data", "kill", 0)
							es.keysetvalue(login_id, "player_data", "death", 0)
							es.keysetvalue(login_id, "player_data", "health", 100)
							es.keysetvalue(login_id, "player_data", "power", 100)
							es.keysetvalue(login_id, "player_data", "speed", 1000)
							es.keysetvalue(login_id, "player_data", "mp", 0)
							es.keysetvalue(login_id, "player_data", "skill1", 0)
							es.keysetvalue(login_id, "player_data", "skill2", 0)
							es.keysetvalue(login_id, "player_data", "skill3", 0)
							es.keysetvalue(login_id, "player_data", "skill4", 0)
							es.keysetvalue(login_id, "player_data", "skill5", 0)
							es.keysetvalue(login_id, "player_data", "skill6", 0)
							es.keysetvalue(login_id, "player_data", "skill7", 0)
							es.keysetvalue(login_id, "player_data", "skill8", 0)
							es.keysetvalue(login_id, "player_data", "skill9", 0)
							es.keysetvalue(login_id, "player_data", "skill10", 0)
							es.keysetvalue(login_id, "player_data", "skill11", 0)
							es.keysetvalue(login_id, "player_data", "skill12", 0)
							es.keysetvalue(login_id, "player_data", "skill13", 0)
							es.keysetvalue(login_id, "player_data", "skill14", 0)
							es.keysetvalue(login_id, "player_data", "skill15", 0)
							es.keysetvalue(login_id, "player_data", "skill16", 0)
							es.keysetvalue(login_id, "player_data", "skill17", 0)
							es.keysetvalue(login_id, "player_data", "skill18", 0)
							es.keysetvalue(login_id, "player_data", "skill19", 0)
							es.keysetvalue(login_id, "player_data", "skill20", 0)
							es.keysetvalue(login_id, "player_data", "item1", 0)
							es.keysetvalue(login_id, "player_data", "item2", 0)
							es.keysetvalue(login_id, "player_data", "item3", 0)
							es.keysetvalue(login_id, "player_data", "item4", 0)
							es.keysetvalue(login_id, "player_data", "item5", 0)
							es.keysetvalue(login_id, "player_data", "item6", 0)
							es.keysetvalue(login_id, "player_data", "item7", 0)
							es.keysetvalue(login_id, "player_data", "item8", 0)
							es.keysetvalue(login_id, "player_data", "item9", 0)
							es.keysetvalue(login_id, "player_data", "item10", 0)
							es.keysetvalue(login_id, "player_data", "item11", 0)
							es.keysetvalue(login_id, "player_data", "item12", 0)
							es.keysetvalue(login_id, "player_data", "item13", 0)
							es.keysetvalue(login_id, "player_data", "item14", 0)
							es.keysetvalue(login_id, "player_data", "item15", 0)
							es.keysetvalue(login_id, "player_data", "item16", 0)
							es.keysetvalue(login_id, "player_data", "item17", 0)
							es.keysetvalue(login_id, "player_data", "item18", 0)
							es.keysetvalue(login_id, "player_data", "item19", 0)
							es.keysetvalue(login_id, "player_data", "item20", 0)
							es.keysetvalue(login_id, "player_data", "item21", 0)
							es.keysetvalue(login_id, "player_data", "item22", 0)
							es.keysetvalue(login_id, "player_data", "item23", 0)
							es.keysetvalue(login_id, "player_data", "item24", 0)
							es.keysetvalue(login_id, "player_data", "item25", 0)
							es.keysetvalue(login_id, "player_data", "item26", 0)
							es.keysetvalue(login_id, "player_data", "item27", 0)
							es.keysetvalue(login_id, "player_data", "item28", 0)
							es.keysetvalue(login_id, "player_data", "item29", 0)
							es.keysetvalue(login_id, "player_data", "item30", 0)
							es.keysetvalue(login_id, "player_data", "item31", 0)
							es.keysetvalue(login_id, "player_data", "item32", 0)
							es.keysetvalue(login_id, "player_data", "item33", 0)
							es.keysetvalue(login_id, "player_data", "item34", 0)
							es.keysetvalue(login_id, "player_data", "item35", 0)
							es.keysetvalue(login_id, "player_data", "item36", 0)
							es.keysetvalue(login_id, "player_data", "item37", 0)
							es.keysetvalue(login_id, "player_data", "item38", 0)
							es.keysetvalue(login_id, "player_data", "item39", 0)
							es.keysetvalue(login_id, "player_data", "item40", 0)
							es.keysetvalue(login_id, "player_data", "unlock_1", 0)
							es.keysetvalue(login_id, "player_data", "unlock_2", 0)
							es.keysetvalue(login_id, "player_data", "unlock_3", 0)
							es.keysetvalue(login_id, "player_data", "unlock_4", 0)
							es.keysetvalue(login_id, "player_data", "unlock_5", 0)
							es.keysetvalue(login_id, "player_data", "unlock_5", 0)
							es.keysetvalue(login_id, "player_data", "unlock_6", 0)
							es.keysetvalue(login_id, "player_data", "unlock_7", 0)
							es.keysetvalue(login_id, "player_data", "unlock_8", 0)
							es.keysetvalue(login_id, "player_data", "unlock_9", 0)
							es.keysetvalue(login_id, "player_data", "unlock_10", 0)
							es.keysetvalue(login_id, "player_data", "unlock_11", 0)
							es.keysetvalue(login_id, "player_data", "unlock_12", 0)
							es.keysetvalue(login_id, "player_data", "unlock_13", 0)
							es.keysetvalue(login_id, "player_data", "unlock_14", 0)
							es.keysetvalue(login_id, "player_data", "unlock_15", 0)
							es.keysetvalue(login_id, "player_data", "unlock_16", 0)
							es.keysetvalue(login_id, "player_data", "unlock_17", 0)
							es.keysetvalue(login_id, "player_data", "unlock_18", 0)
							es.keysetvalue(login_id, "player_data", "unlock_19", 0)
							es.keysetvalue(login_id, "player_data", "unlock_20", 0)
							es.keysetvalue(login_id, "player_data", "count_unlock_3", 0)
							es.keysetvalue(login_id, "player_data", "count_unlock_4", 0)
							es.keysetvalue(login_id, "player_data", "count_unlock_5", 0)
							es.keysetvalue(login_id, "player_data", "count_unlock_6", 0)
							es.keysetvalue(login_id, "player_data", "count_unlock_7", 0)
							es.keysetvalue(login_id, "player_data", "count_unlock_8", 0)
							es.keysetvalue(login_id, "player_data", "count_unlock_9", 0)
							es.keysetvalue(login_id, "player_data", "count_unlock_10", 0)
							es.keysetvalue(login_id, "player_data", "count_unlock_11", 0)
							es.keysetvalue(login_id, "player_data", "count_unlock_12", 0)
							es.keysetvalue(login_id, "player_data", "count_unlock_13", 0)
							es.keysetvalue(login_id, "player_data", "count_unlock_14", 0)
							es.keysetvalue(login_id, "player_data", "count_unlock_15", 0)
							es.keysetvalue(login_id, "player_data", "count_unlock_16", 0)
							es.keysetvalue(login_id, "player_data", "count_unlock_17", 0)
							es.keysetvalue(login_id, "player_data", "count_unlock_18", 0)
							es.keysetvalue(login_id, "player_data", "count_unlock_19", 0)
							es.keysetvalue(login_id, "player_data", "count_unlock_20", 0)
							es.keysetvalue(login_id, "player_data", "code", "없음 ")
							es.keysetvalue(login_id, "player_data", "mastery", "없음 ")
							es.keysetvalue(login_id, "player_data", "mastery_unlock_1", 0)
							es.keysetvalue(login_id, "player_data", "mastery_unlock_2", 0)
							es.keysetvalue(login_id, "player_data", "mastery_unlock_3", 0)
							es.keysetvalue(login_id, "player_data", "mastery_unlock_4", 0)
							es.keysetvalue(login_id, "player_data", "mastery_unlock_5", 0)
							es.keysetvalue(login_id, "player_data", "mastery_unlock_6", 0)
							es.keysetvalue(login_id, "player_data", "bp", 0)
							es.keysetvalue(login_id, "player_data", "money", 0)
							es.keysetvalue(login_id, "player_data", "human_xp", 0)
							es.keysetvalue(login_id, "player_data", "supporter_time", 7200)
							es.keysetvalue(login_id, "player_data", "stetpoint", 1)
							es.keysetvalue(login_id, "player_data", "skillpoint", 1)
							es.keysetvalue(login_id, "player_data", "hegrenade_damage_min", 100)
							es.keysetvalue(login_id, "player_data", "hegrenade_damage_max", 444)
							es.keysetvalue(login_id, "player_data", "jump_count", 0)
							es.keysetvalue(login_id, "player_data", "fire_count", 0)
							es.keysetvalue(login_id, "player_data", "main_storyroute", 1)
							es.keysetvalue(login_id, "player_data", "play_time", 0)
							es.keysetvalue(login_id, "player_data", "update_version", 4)
							es.keygroupsave(login_id, "|bot/player_data")
def israining():
	if es.getentityindex("func_precipitation") > 0: return 1
	else: return 0

def Commander4(userid, args):
	steamid = es.getplayersteamid(userid)
	username = es.getplayername(userid)
	if steamid != "BOT":
		ff = args[0]
		if ff == "yoo":
			x,y,z = es.getplayerlocation(userid)
			for fuserid in getbot():
				bot_move(fuserid, x, y, z)
			return False
		if ff == "jointeam":
			if int(args[1]) != int(sv('zombieteam')):
				es.changeteam(userid, args[1])
		if ff.lower() == "explode":
			return False
		if ff.lower() == "kill":
			return False
		if ff.lower() == "loc":
			x,y,z = es.getplayerlocation(userid)
			esc.tell(userid, " %s %s %s" %(x,y,z))
		if args[0] == "!automatic_login":
			if len(args) == 3:
				login_id = args[1]
				login_password = args[2]
				es.keysetvalue("total_players", steamid, "automatic_id", login_id)
				es.keysetvalue("total_players", steamid, "automatic_password", login_password)
				esc.tell(userid, "#255,255,255자동 로그인 세팅이 되었습니다. 이제 접속하면 자동으로 이 계정으로 로그인됩니다.")
				es.keygroupsave("total_players", "|bot/server_data")
		if args[0] == "!change_password" and len(args) == 4:
			login_id = args[1]
			login_password = args[2]
			change_password = args[3]
			if str(es.keygetvalue("total_players", steamid, "register_id")) == str(login_id):
				check_2 = est.fileexists("addons/eventscripts/bot/player_data/es_%s_db.txt" %(login_id))
				if check_2 == 1:
					existcheck = es.exists("keygroup", login_id)
					if existcheck == 0: es.keygroupload(login_id, "|bot/player_data")
					real_password = str(es.keygetvalue(login_id, "player_data", "password"))
					if real_password == str(login_password):
						es.keysetvalue(login_id, "player_data", "password", login_password)
						esc.tell(userid, "#255,255,255성공적으로 패스워드 변경이 되었습니다.")
					es.keygroupsave(login_id, "|bot/player_data")
					if existcheck == 0: es.keygroupdelete(login_id, "|bot/player_data")
		if args[0] == "!find_id":
			if len(args) == 2:
				login_id = str(args[1])
				check_2 = est.fileexists("addons/eventscripts/bot/player_data/es_%s_db.txt" %(login_id))
				if check_2 == 1:
					allcheck = es.exists("keygroup", login_id)
					if allcheck == 0: es.keygroupload(login_id, "|bot/player_data")
					question = str(es.keygetvalue(login_id, "player_data", "password_question"))
					esc.tell(userid, "#255,255,255＊ %s 아이디에 등록된 찾기 질문 : %s" %(login_id, question))
					if allcheck == 0: es.keygroupdelete(login_id)
					return False
				else: esc.tell(userid, "#255,255,255존재하지 않는 계정입니다.")
		if args[0] == "!answer_id":
			if len(args) == 3:
				login_id = str(args[1])
				answer = "%s " %(str(args[2]))
				answer = answer.lower()
				check_2 = est.fileexists("addons/eventscripts/bot/player_data/es_%s_db.txt" %(login_id))
				if check_2 == 1:
					allcheck = es.exists("keygroup", login_id)
					if allcheck == 0: es.keygroupload(login_id, "|bot/player_data")
					qanswer = str(es.keygetvalue(login_id, "player_data", "password_answer"))
					qanswer = qanswer.lower()
					if qanswer == answer:
						password = es.keygetvalue(login_id, "player_data", "password")
						usermsg.echo(userid, "%s 계정의 패스워드 : %s" %(login_id, password))
					else:
						question = str(es.keygetvalue(login_id, "player_data", "password_question"))
						esc.tell(userid, "#255,255,255＊ 틀렸습니다. %s 아이디에 등록된 찾기 질문 : %s" %(login_id, question))
					if allcheck == 0: es.keygroupdelete(login_id)
					return False
				else: esc.tell(userid, "#255,255,255존재하지 않는 계정입니다.")
		if args[0] == "!register":
			if int(es.keygetvalue("total_players", steamid, "register")) == 0:
				if len(args) >= 1:
					login_id = str(args[1])
					login_id = login_id.lower()
					password = str(args[2])
					check = es.exists("keygroup", login_id)
					if check == 0:
						check_2 = est.fileexists("addons/eventscripts/bot/player_data/es_%s_db.txt" %(login_id))
						if check_2 == 0:
							es.keygroupcreate(login_id)
							es.keycreate(login_id, "player_data")
							es.keysetvalue(login_id, "player_data", "password", password)
							es.keysetvalue(login_id, "player_data", "level", 1)
							es.keysetvalue(login_id, "player_data", "xp", 0)
							es.keysetvalue(login_id, "player_data", "nextxp", 10)
							es.keysetvalue(login_id, "player_data", "kill", 0)
							es.keysetvalue(login_id, "player_data", "death", 0)
							es.keysetvalue(login_id, "player_data", "health", 100)
							es.keysetvalue(login_id, "player_data", "power", 100)
							es.keysetvalue(login_id, "player_data", "speed", 1000)
							es.keysetvalue(login_id, "player_data", "mp", 0)
							es.keysetvalue(login_id, "player_data", "skill1", 0)
							es.keysetvalue(login_id, "player_data", "skill2", 0)
							es.keysetvalue(login_id, "player_data", "skill3", 0)
							es.keysetvalue(login_id, "player_data", "skill4", 0)
							es.keysetvalue(login_id, "player_data", "skill5", 0)
							es.keysetvalue(login_id, "player_data", "skill6", 0)
							es.keysetvalue(login_id, "player_data", "skill7", 0)
							es.keysetvalue(login_id, "player_data", "skill8", 0)
							es.keysetvalue(login_id, "player_data", "skill9", 0)
							es.keysetvalue(login_id, "player_data", "skill10", 0)
							es.keysetvalue(login_id, "player_data", "item1", 0)
							es.keysetvalue(login_id, "player_data", "item2", 0)
							es.keysetvalue(login_id, "player_data", "item3", 0)
							es.keysetvalue(login_id, "player_data", "item4", 0)
							es.keysetvalue(login_id, "player_data", "item6", 0)
							es.keysetvalue(login_id, "player_data", "item7", 0)
							es.keysetvalue(login_id, "player_data", "item8", 0)
							es.keysetvalue(login_id, "player_data", "item9", 0)
							es.keysetvalue(login_id, "player_data", "item10", 0)
							es.keysetvalue(login_id, "player_data", "item11", 0)
							es.keysetvalue(login_id, "player_data", "item12", 0)
							es.keysetvalue(login_id, "player_data", "item13", 0)
							es.keysetvalue(login_id, "player_data", "item14", 0)
							es.keysetvalue(login_id, "player_data", "item15", 0)
							es.keysetvalue(login_id, "player_data", "item16", 0)
							es.keysetvalue(login_id, "player_data", "item17", 0)
							es.keysetvalue(login_id, "player_data", "item18", 0)
							es.keysetvalue(login_id, "player_data", "item19", 0)
							es.keysetvalue(login_id, "player_data", "item20", 0)
							es.keysetvalue(login_id, "player_data", "unlock_1", 0)
							es.keysetvalue(login_id, "player_data", "unlock_2", 0)
							es.keysetvalue(login_id, "player_data", "unlock_3", 0)
							es.keysetvalue(login_id, "player_data", "unlock_4", 0)
							es.keysetvalue(login_id, "player_data", "unlock_5", 0)
							es.keysetvalue(login_id, "player_data", "unlock_5", 0)
							es.keysetvalue(login_id, "player_data", "unlock_6", 0)
							es.keysetvalue(login_id, "player_data", "unlock_7", 0)
							es.keysetvalue(login_id, "player_data", "unlock_8", 0)
							es.keysetvalue(login_id, "player_data", "unlock_9", 0)
							es.keysetvalue(login_id, "player_data", "unlock_10", 0)
							es.keysetvalue(login_id, "player_data", "unlock_11", 0)
							es.keysetvalue(login_id, "player_data", "unlock_12", 0)
							es.keysetvalue(login_id, "player_data", "unlock_13", 0)
							es.keysetvalue(login_id, "player_data", "unlock_14", 0)
							es.keysetvalue(login_id, "player_data", "unlock_15", 0)
							es.keysetvalue(login_id, "player_data", "code", "없음 ")
							es.keysetvalue(login_id, "player_data", "bp", 0)
							es.keysetvalue(login_id, "player_data", "money", 0)
							es.keysetvalue(login_id, "player_data", "human_xp", 0)
							es.keysetvalue(login_id, "player_data", "supporter_time", 7200)
							es.keysetvalue(login_id, "player_data", "stetpoint", 1)
							es.keysetvalue(login_id, "player_data", "skillpoint", 1)
							es.keysetvalue(login_id, "player_data", "main_storyroute", 1)
							es.keysetvalue(login_id, "player_data", "update_version", 6)
							es.keygroupsave(login_id, "|bot/player_data")
							es.keygroupdelete(login_id)
							es.keysetvalue("total_players", steamid, "register", 1)
							es.keysetvalue("total_players", steamid, "register_id", login_id)
							esc.tell(userid, "#255,255,255계정이 생성되었습니다. 로그인하세요!")
							es.keygroupsave("total_players", "|bot/server_data")
							return False
						else: esc.tell(userid, "#255,255,255이미 만들어진 계정입니다.")
					else: esc.tell(userid, "#255,255,255이미 온라인 상태인 계정입니다.")
			else: esc.tell(userid, "#255,255,255당신은 이미 계정을 만들었습니다!")
		if args[0] == "!login":
			login_id = getplayerid(userid)
			if login_id == "":
				if len(args) == 3:
					login_id = str(args[1])
					login_id = login_id.lower()
					password = str(args[2])
					check = es.exists("keygroup", login_id)
					register_id = str(es.keygetvalue("total_players", steamid, "register_id"))
					check_2 = est.fileexists("addons/eventscripts/bot/player_data/es_%s_db.txt" %(login_id))
					if check_2 == 0: check = 1
					if check == 0:
						es.keygroupload(login_id, "|bot/player_data")
						ste = es.getplayersteamid(userid)
						ste = ste.replace("STEAM_", "")
						ste = ste.replace(":", "")
						passwordok = 0
						if password == str(es.keygetvalue(login_id, "player_data", "password")): passwordok = 1
						if str(login_id) == str(ste):
							if str(register_id) == int(ste):
								passwordok = 1
						if passwordok == 1:
							id[userid] = login_id
							#esc.tell(userid, "#255,255,255로그인 되었습니다!")
							es.keysetvalue(login_id, "player_data", "userid", userid)
						else:
							es.keygroupdelete(login_id)
							esc.tell(userid, "#255,255,255패스워드가 일치하지 않습니다.")
					else: esc.tell(userid, "#255,255,255이미 온라인 상태인 계정이거나 없는 계정입니다.")
			else: esc.tell(userid, "#255,255,255이미 당신은 로그인한 상태입니다.")
		if args[0] == "jointeam":
			login_id = getplayerid(userid)
			if login_id == "":
				ste = es.getplayersteamid(userid)
				ste = ste.replace("STEAM_", "")
				ste = ste.replace(":", "")
				es.server.cmd('es_xsexec %s !register "%s" "102579" "n", "nz"' %(userid, ste))
				es.server.cmd('es_xsexec %s !login "%s" "102579"' %(userid, ste))
				return True
		if args[0] == "!helpz":
			esc.tell(userid, "#255,255,255!make_npc 모델 이름 모션")
		if args[0] == "!make_npc":
			model = args[1]
			if model == "!robot": model = "props/cs_office/vending_machine"
			name = args[2]
			seq = args[3]
			ang = es.getplayerprop(userid, "CCSPlayer.m_angEyeAngles[1]")
			x,y,z = es.getplayerlocation(userid)
			esc.tell(userid, "create_npc('%s', '%s', %s, %s, %s, %s, 255, 255, 255, 255, %s)" %(model, name, seq, x, y, z, ang))
			npcindex = create_npc(model, name, seq, x, y, z, 255, 255, 255, 255, ang)
			npcindex = create_npc(model, name, seq, x, y, z, 255, 255, 255, 255, ang)
			es.setindexprop(npcindex, "CAI_BaseNPC.baseclass.baseclass.baseclass.baseclass.baseclass.m_CollisionGroup", 2)
		if args[0] == "cheer":
			alive = est.isalive(userid)
			if alive:
				login_id = getplayerid(userid)
				buymenu = popuplib.easymenu('buymenu_%s' %(userid), None, buymenu_select)
				buymenu.settitle("Buy Menu")
				for a in BUYMENU_LIST_PRINT:
					state = 1
					lockcheck = 0
					if BUYMENU_LIST[a]['skill_max'] > 0:
						skillname = BUYMENU_LIST[a]['skill']
						if int(es.keygetvalue("buymenu", userid, skillname)) >= BUYMENU_LIST[a]['skill_max']:
							state = 0
					if BUYMENU_LIST[a]['need_unlock'] != "None":
						unlock_name = BUYMENU_LIST[a]['need_unlock']
						if int(es.keygetvalue(login_id, "player_data", unlock_name)) <= 0:
							state = 0
							lockcheck = 1
					need_level = BUYMENU_LIST[a]['need_level']
					if int(need_level) == -1: continue
					if need_level > int(es.keygetvalue(login_id, "player_data", "level")):
						state = 0
					dollar = BUYMENU_LIST[a]['dollar']
					curskill = 0
					skillname = BUYMENU_LIST[a]['skill']
					if skillname != "None":
						curskill = int(es.keygetvalue("buymenu", userid, skillname))
					max = BUYMENU_LIST[a]['skill_max']
					mp = BUYMENU_LIST[a]['mp']
					if lockcheck == 1: lock_print = "{LOCKED}"
					if lockcheck == 0: lock_print = ""
					print_k = "%s [%s/%s] %s(Lv.%s)($%s)(MP %s)" %(a, curskill, max, lock_print, need_level, dollar, mp)
					print_k = print_k.replace(" [0/0]", "")
					print_k = print_k.replace("($0)", "")
					print_k = print_k.replace("(MP 0)", "")
					print_k = print_k.replace("(Lv.1)", "")
					buymenu.addoption(a, print_k, state)
				buymenu.send(userid)
				popuplib.delete('buymenu_%s' %(userid))
		if args[0] == "nightvision":
			es.server.cmd('es_xsexec %s -sm_entcontrol_grab' %(userid))
			if themap() in str(REST_MAPS):
				alive = est.isalive(userid)
				if alive == 0: est.spawn(userid)
				if alive > 0:
					propid = est.getviewprop(userid)
					npcname = es.entitygetvalue(propid, "classname")
					npc_split = npcname.split()
					if "npc_teleport" in str(npc_split[0]):
						nl = es.getindexprop(propid, "CBaseEntity.m_vecOrigin").split(",")
						victim_location = vecmath.vector(es.getplayerlocation(userid))
						attacker_location = vecmath.vector(es.getindexprop(propid, "CBaseEntity.m_vecOrigin").split(","))
						distance = vecmath.distance(victim_location, attacker_location) * 0.0254
						if distance <= 3:
							es.setpos(userid, npc_split[1], npc_split[2], npc_split[3])
							return False
					if "npc" in npcname:
						nl = es.getindexprop(propid, "CBaseEntity.m_vecOrigin").split(",")
						victim_location = vecmath.vector(es.getplayerlocation(userid))
						attacker_location = vecmath.vector(es.getindexprop(propid, "CBaseEntity.m_vecOrigin").split(","))
						distance = vecmath.distance(victim_location, attacker_location) * 0.0254
						if distance <= 3:
							login_id = getplayerid(userid)
							quest = int(es.keygetvalue(login_id, "player_data", "main_storyroute"))
							if npcname == "npc_custom_nightfever":
								custom_p.send(userid)
							if npcname == "npc_tenji_nightfever":
								if quest == 1 or quest == 2:
									quest_box = popuplib.create('quest_box_%s %s' %(userid, quest))
									quest_box.addline(" ")
									quest_box.addline("＠ 텐지의 심부름")
									quest_box.addline(" ")
									quest_box.addline("“ 준페이가 밖에서 맥주 하나를 시키더군. 하지만 난 나갈수가 없는 상황이야.")
									quest_box.addline("나 대신 그에게 맥주와 편지를 전해줄수 있겠나? ”")
									quest_box.addline(" ")
									if quest == 1: quest_box.addline("->1. 수락")
									quest_box.addline("0. 닫기")
									quest_box.addline(" ")
									quest_box.menuselect = quest_select
									quest_box.send(userid)
									popuplib.delete('quest_box_%s %s' %(userid, quest))
							if "gay" in npcname:
								cah = random.choice(["ang", "ohmy", "fuckyou"])
								if "gaygate" in npcname: cah = "fuckyou"
								es.emitsound("entity", propid, "zeisenproject_-1/autosounds/gay/%s.mp3" %(cah), 1.0, 1.0)
							if npcname == "npc_horror1_nightfever":
								es.emitsound("entity", propid, "zeisenproject_-1/autosounds/story_sounds/wsound_5.wav", 1.0, 1.0)
								n_route = str(sv('n_route'))
								if len(n_route) == 8:
									n_route = ""
									usermsg.hudhint(userid, "날 이상한 눈으로 보고있다...")
								n_route = "%sr" %(n_route)
								if int(es.getentityindex("npc_horror4_nightfever")) <= 0:
									if n_route == "rrrrrrrr":
										est.play("#h", "zeisenproject_-1/autosounds/story_sounds/wsound_4.wav")
										create_npc('error.mdl', 'npc_horror4_nightfever', 0, 527.82232666, 2373.73266602, 32.03125, 255, 255, 255, 255, -1.41406035423)
										create_npc('error.mdl', 'npc_horror4_nightfever', 0, 527.82232666, 2373.73266602, 32.03125, 255, 255, 255, 255, -1.41406035423)
								es.set("n_route", n_route)
							if npcname == "npc_horror2_nightfever":
								es.emitsound("entity", propid, "zeisenproject_-1/autosounds/story_sounds/wsound_6.wav", 1.0, 1.0)
								n_route = str(sv('n_route'))
								if len(n_route) == 8:
									n_route = ""
									usermsg.hudhint(userid, "날 이상한 눈으로 보고있다...")
								n_route = "%sb" %(n_route)
								if int(es.getentityindex("npc_horror3_nightfever")) <= 0:
									if n_route == "rbrbrbrb":
										est.play("#h", "zeisenproject_-1/autosounds/story_sounds/wsound_4.wav")
										create_npc('models/error.mdl', 'npc_horror3_nightfever', 0, 809.407531738, 2406.98144531, 32, 255, 255, 255, 255, -90)
										create_npc('models/error.mdl', 'npc_horror3_nightfever', 0, 809.407531738, 2406.98144531, 32, 255, 255, 255, 255, -90)
									if n_route == "rrbbrrbb":
										est.play("#h", "zeisenproject_-1/autosounds/story_sounds/wsound_4.wav")
										create_npc('error.mdl', 'npc_horror5_nightfever', 0, 1056.33886719, 2403.72460938, 32.03125, 255, 255, 255, 255, -137.813766479)
										create_npc('error.mdl', 'npc_horror5_nightfever', 0, 1056.33886719, 2403.72460938, 32.03125, 255, 255, 255, 255, -137.813766479)
								es.set("n_route", n_route)
							if npcname == "npc_horror3_nightfever":
								if str(sv('n_route')) == "rrrrbbbb":
									usermsg.hudhint(userid, "아, 그 체인이 글쎄, 내 아이를 가져갔지 뭐야. 내 소중한 딸 레이센을.. 아... 7년동안 이나 못봤는데...")
								else:
									usermsg.hudhint(userid, "아, 그 ──이 글쎄, 내 ──를 가져갔지 뭐야. 내 소중한 ─ ───을.. 아... 7─── ── 못봤는데...")
							if npcname == "npc_horror4_nightfever":
								n_route = str(sv('n_route'))
								ddmsg = "너는 %s" %(n_route)
								usermsg.hudhint(userid, ddmsg)
							if npcname in NPC_LIST:
								npc_allow = 1
								human_xp = int(es.keygetvalue(login_id, "player_data", "human_xp"))
								npc_xp = NPC_LIST[npcname]['npc_xp']
								if human_xp >= npc_xp:
									raining = es.getentityindex("func_precipitation")
									if raining > 0: text = random.choice(NPC_LIST[npcname]['npc_rain_chat'])
									else: text = random.choice(NPC_LIST[npcname]['npc_chat'])
									npc_popup = NPC_LIST[npcname]['npc_popup']
									if str(npc_popup) != "-1":
										popuplib.send(npc_popup, userid)
									if npcname == "npc_reisen_nightfever":
										if quest == 3 or quest == 4:
											quest_box = popuplib.create('quest_box_%s %s' %(userid, quest))
											quest_box.addline(" ")
											quest_box.addline("＠ 레이센의 악몽")
											quest_box.addline(" ")
											quest_box.addline("“ 제가 꿈을 꿨는데.. 정말 신비하면서 이상한 꿈을 꾼거 같아요.")
											quest_box.addline("꿈 같은데... 너무 생생해요... 진짜인지 찾아주세요! ”")
											quest_box.addline(" ")
											if quest == 3: quest_box.addline("->1. 수락")
											quest_box.addline("0. 닫기")
											quest_box.addline(" ")
											quest_box.menuselect = quest_select
											quest_box.send(userid)
											popuplib.delete('quest_box_%s %s' %(userid, quest))
									if npcname == "npc_junpei_nightfever":
										if quest == 2:
											text = "오오! 드디어 온건가! 돈은 여깄어. 500엔."
											keymath(login_id, "player_data", "money", "+", 500)
											es.keysetvalue(login_id, "player_data", "main_storyroute", 3)
									name = NPC_LIST[npcname]['npc_name']
									if str(text) != "123456789":
										esc.tell(userid, "%s :#default %s" %(name, text))
									if npcname == "npc_sonic_nightfever":
										total_count = 0
										distance_count = 0
										for fuserid in getalivehuman():
											total_count += 1
											nl = es.getindexprop(propid, "CBaseEntity.m_vecOrigin").split(",")
											victim_location = vecmath.vector(es.getplayerlocation(fuserid))
											attacker_location = vecmath.vector(es.getindexprop(propid, "CBaseEntity.m_vecOrigin").split(","))
											distancee = vecmath.distance(victim_location, attacker_location) * 0.0254
											if float(distancee) <= 5: distance_count += 1
										if (distance_count * 2) >= total_count:
											#vote_list = ["cs_assault2_goban_b3"]
											#if int(sv('event_chance')) == 1:
											#	for a in SERVER_UNLOCK_LIST:
											#		vote_list.append(a)
											#abc = "NNN"
											#for b in vote_list:
											#	if abc == "NNN":
											#		abc = "%s" %(b)
											#	else: abc = "%s %s" %(abc, b)
											#es.server.cmd('es_xsoon sm_votemap %s' %(abc))
											if votelib.exists('change_vote'):
												if not votelib.isrunning('change_vote'):
													changemap_vote("f")
											else:
												changemap_vote("f")
										#sonic_npc = popuplib.easymenu('sonic_npc', None, npc_select)
										#sonic_npc.settitle("＠ Sonic")
										#sonic_npc.c_endsep = " \nNPC와 특별한걸 할수 있습니다.\n "
										#popuplib.delete('sonic_npc')
									if str(NPC_LIST[npcname]['npc_info']) != "None": usermsg.hudhint(userid, NPC_LIST[npcname]['npc_info'])
								else:
									name = NPC_LIST[npcname]['npc_name']
									negative_msg = random.choice(NPC_LIST[npcname]['npc_negative_msg'])
									esc.tell(userid, "%s :#default %s" %(name, negative_msg))
									usermsg.hudhint(userid, "※ 나를 거부하는듯 하다... 더 많은 인기도가 필요하다.")
					else:
						nl = es.getindexprop(propid, "CBaseEntity.m_vecOrigin").split(",")
						victim_location = vecmath.vector(es.getplayerlocation(userid))
						attacker_location = vecmath.vector(es.getindexprop(propid, "CBaseEntity.m_vecOrigin").split(","))
						distance = vecmath.distance(victim_location, attacker_location) * 0.0254
	return True
########################################################################################### Fuctions

def one_damage_reset(userid):
	one_damage[userid] = 0

def one_damage_armor_reset(userid):
	one_damage_armor[userid] = 0

def quest_select(userid, choice, popupname):
	login_id = getplayerid(userid)
	popupname_args = popupname.split()
	quest = int(popupname_args[1])
	if quest == 1:
		npc_tell(userid, "#255,0,0텐지", "고맙네, 답례는 그가 줄것이야.")
		npc_tell(userid, "#255,0,0텐지", "그는 밤에만 온다네. 잘 찾아보면 있을것이야...")
		quest = 2
	if quest == 3:
		npc_tell(userid, "#0,0,255레이센", "정말 고맙습니다! 꼭 찾으시길 빌게요.")
		quest = 4
	es.keysetvalue(login_id, "player_data", "main_storyroute", quest)

def make_dark():
	ent = es.createentity("light_dynamic")
	es.entitysetvalue(ent, "brightness", 1)
	es.entitysetvalue(ent, "style", 1)
	es.entitysetvalue(ent, "distance", 9999.0)
	es.entitysetvalue(ent, "spotlight_radius", 9999.0)
	es.spawnentity(ent)
	es.set("what_ent", ent)
	est.setentitycolor(ent, 0, 0, 255, 255)

def unlock(args):
	userid = int(args[0])
	team = es.getplayerteam(userid)
	username = es.getplayername(userid)
	if team <= 1: esc.msg("#white %s#default님이#darkgreen %s 도전 과제를 달성하였습니다." %(username, args[1]))
	if team == 2: esc.msg("#red %s#default님이#darkgreen %s 도전 과제를 달성하였습니다." %(username, args[1]))
	if team == 3: esc.msg("#blue %s#default님이#darkgreen %s 도전 과제를 달성하였습니다." %(username, args[1]))
	est.play("#h", "ui/achievement_earned.wav")

def nightfever_close():
	bgm_loop.stop()
	est.stopsound("#h", "zeisenproject_-1/de_nightfever/%s.mp3" %(sv('today')))
	est.play("#h", "ambient/alarms/combine_bank_alarm_loop4.wav")
	fade_red()
	zzz = repeat.create('zzz', fade_red, ())
	zzz.start(1.2, 17)
	gamethread.delayed(22, nightfever_close2, ())

def nightfever_close3():
	es.server.cmd('sv_password nipperkk')
	nightfever_dead()

def nightfever_close2():
	est.stopsound("#h", "ambient/alarms/combine_bank_alarm_loop4.wav")
	est.play("#h", "zeisenproject_-1/autosounds/nightfever_close.mp3")
	gamethread.delayed(1, nightfever_dead, ())
	gamethread.delayed(1, es.server.cmd, ("sv_password nipperkk"))

def nightfever_dead():
	for index in es.createentityindexlist(""):
		classname = es.entitygetvalue(index, "classname")
		if "npc" in classname: est.dissolve(classname)

def fade_red():
	est.fade("#h", 1, 0.1, 0.1, 255, 0, 0, 125)
	gamethread.delayed(0.2, est.fade, ("#h", 0, 0.2, 0.2, 255, 0, 0, 125))

def weaponswap(args):
	userid = int(args[0])
	weapon_name = "weapon_%s" %(args[1])
	weapon_index = est.getweaponindex(userid, weapon_name)
	if es.isbot(userid):
		username = es.getplayername(userid)
		#if "[Bomber]" in username:
		es.setindexprop(weapon_index, "CBaseCombatWeapon.LocalActiveWeaponData.m_flNextPrimaryAttack", 1)
		es.setindexprop(weapon_index, "CBaseCombatWeapon.LocalActiveWeaponData.m_flNextSecondaryAttack", 1)
		es.setplayerprop(userid, "CCSPlayer.baseclass.baseclass.bcc_localdata.m_flNextAttack", 1)
	else:
		r,g,b,a = getentitycolor(weapon_index)
		me_clip = est.getclipammo(userid, weapon_name)
		me_ammo = est.getammo(userid, weapon_name)
		me_cash = es.getplayerprop(userid, _moneyprop)
		usermsg.hudmsg(userid, "%s Cash\n%s/%s" %(me_cash, me_clip, me_ammo), 1, 0.9, 0.93, r1=r, g1=g, b1=b)
		login_id = getplayerid(userid)
		mastery = str(es.keygetvalue(login_id, "player_data", "mastery"))
		if mastery == "용병(SR) ":
			time = getgametime()
			attacktime = float(es.getplayerprop(userid, 'CCSPlayer.baseclass.baseclass.bcc_localdata.m_flNextAttack'))
			check = 1.5
			delay = (attacktime - time)
			delay = delay / check
			settime = time + delay
			es.setindexprop(weapon_index, "CBaseCombatWeapon.LocalActiveWeaponData.m_flNextPrimaryAttack", settime)
			es.setindexprop(weapon_index, "CBaseCombatWeapon.LocalActiveWeaponData.m_flNextSecondaryAttack", settime)
			es.setplayerprop(userid, "CCSPlayer.baseclass.baseclass.bcc_localdata.m_flNextAttack", settime)
			lists = es.createentityindexlist('predicted_viewmodel')
			for a in lists:
				rate = float(es.getindexprop(a, 'CPredictedViewModel.baseclass.m_flPlaybackRate'))
				if rate > 0:
					if es.getplayerhandle(userid) == int(es.getindexprop(a, 'CPredictedViewModel.baseclass.m_hOwner')):
						view_index = a
			rate = float(es.getindexprop(view_index, 'CPredictedViewModel.baseclass.m_flPlaybackRate')) * check
			es.setindexprop(view_index, 'CPredictedViewModel.baseclass.m_flPlaybackRate', rate)
		if weapon_name == "weapon_knife":
			if int(es.keygetvalue(login_id, "player_data", "item1")) > 0:
				pf = es.precachemodel("models/weapons/w_stunbaton.mdl")
				es.setindexprop(weapon_index, "CBaseCombatWeapon.m_iWorldModelIndex", pf)

def test424():
	userid = 19
	x,y,z = es.getplayerlocation(userid)
	thandle = es.getplayerhandle(userid)
	fake_hegrenade_explosion(x, y, z, thandle)

def fake_hegrenade_explosion(x, y, z, handle=None):
 
    entity = createEntity('hegrenade_projectile')
 
    hegrenade = SPEGrenade.get_instance_from_pointer(entity)
 
    hegrenade.origin = [x, y, z]
 
    hegrenade.damage = 100
 
    hegrenade.islive = True
 
    hegrenade.radius = 350
 
    if not handle is None:
 
        hegrenade.thrower = handle
 
    hegrenade.spawn()
 
    SPEHEGrenade(hegrenade.index).detonate()
 

 

 
def fake_flashbang_detonation(x, y, z, handle=None):
 
    entity = createEntity('flashbang_projectile')
 
    flashbang = SPEGrenade.get_instance_from_pointer(entity)
 
    flashbang.origin = [x, y, z]
 
    flashbang.islive = True
 
    if not handle is None:
 
        flashbang.thrower = handle
 
    flashbang.spawn()
 
    SPEFlashbang(flashbang.index).detonate() 

def buymenu_select(userid, choice, popupnname):
	if est.isalive(userid):
		login_id = getplayerid(userid)
		menu_skill = BUYMENU_LIST[choice]['skill']
		menu_dollar = BUYMENU_LIST[choice]['dollar']
		menu_mp = BUYMENU_LIST[choice]['mp']
		menu_level = BUYMENU_LIST[choice]['need_level']
		menu_max = int(BUYMENU_LIST[choice]['skill_max'])
		userteam = es.getplayerteam(userid)
		if es.getplayerprop(userid, _moneyprop) >= menu_dollar:
			if current_mp[userid] >= menu_mp:
				if current_mp[userid] >= menu_mp:
					if int(es.keygetvalue(login_id, "player_data", "level")) >= menu_level:
						choice_allow = 1
						if menu_skill != "None":
							if int(es.keygetvalue("buymenu", userid, menu_skill)) >= menu_max:
								return
						if choice == "Remote Human" or "Human :" in choice:
							check = es.getuserid("[Human] 스트레이트 킹")
							if check <= 0:
								esc.tell(userid, "기본 아군 봇이 존재하지 않습니다.")
								return
						if choice == "C4":
							if userteam != 2:
								esc.tell(userid, "테러리스트 팀이 아닙니다.")
								return
						if choice == "Be Doctor":
							if int(sv('round')) == 8:
								esc.tell(userid, "라운드 종료 시간엔 이용할수 없습니다.")
								return
						if choice_allow == 1:
							C = -1
							if menu_skill != "None":
								C = keymath("buymenu", userid, menu_skill, "+", 1)
							est.cashadd(userid, -(menu_dollar))
							current_mp[userid] -= menu_mp
							username = es.getplayername(userid)
							C_print = int(C)
							if C > 0:
								if C == int(BUYMENU_LIST[choice]['skill_max']): C_print = "Max"
							if C == -1:
								esc.msg("#blue %s 유저#255,255,255가 #lightgreen%s 아이템#255,255,255을 구매했습니다." %(username, choice))
							else:
								esc.msg("#blue %s 유저#255,255,255가 #lightgreen%s 아이템 #0,255,255(%s 단계)#255,255,255을 구매했습니다." %(username, choice, C_print))
							if choice == "Armor + 4":
								est.armoradd(userid, 4)
								es.emitsound("player", userid, "items/smallmedkit1.wav", 1.0, 1.0)
							if choice == "Armor + 20":
								est.armoradd(userid, 20)
								es.emitsound("player", userid, "items/smallmedkit1.wav", 1.0, 1.0)
							if choice == "Unlimited Ammo":
								est.setammo(userid, 1, 999)
								est.setammo(userid, 2, 999)
							if choice == "HE":
								index = est.getweaponindex(userid, "weapon_hegrenade")
								if index <= 0:
									est.give(userid, "weapon_hegrenade")
								else:
									hegrenade_count = est.getammo(userid, "weapon_hegrenade") + 1
									est.setammo(userid, "weapon_hegrenade", hegrenade_count)
							if choice == "Bomberman":
								index = est.getweaponindex(userid, "weapon_hegrenade")
								if index <= 0:
									est.give(userid, "weapon_hegrenade")
								est.setammo(userid, "weapon_hegrenade", 999)
							if choice == "Flashbang":
								index = est.getweaponindex(userid, "weapo_flashbang")
								if index <= 0:
									est.give(userid, "weapon_flashbang")
								else:
									flashbang_count = est.getammo(userid, "weapon_flashbang") + 1
									est.setammo(userid, "weapon_flashbang", flashbang_count)
							if choice == "C4": est.give(userid, "weapon_c4")
							if choice == "Human : Be Shotgunner":
								for fuserid in getbot():
									if es.getplayerteam(fuserid) == int(sv('humanteam')):
										if est.isalive(fuserid):
											est.removeweapon(fuserid, 1)
											est.give(fuserid, "weapon_m3")
											H = int(es.getplayerprop(fuserid, _healthprop)) + 200
											es.setplayerprop(fuserid, _healthprop, H)
							if choice == "Human : Be Sniper":
								for fuserid in getbot():
									if es.getplayerteam(fuserid) == int(sv('humanteam')):
										if est.isalive(fuserid):
											est.removeweapon(fuserid, 1)
											est.give(fuserid, "weapon_sg550")
							if choice == "Human : Be Juggernut":
								for a_userid in getbot():
									if es.getplayerteam(a_userid) == int(sv('humanteam')):
										if est.isalive(a_userid):
											est.removeweapon(a_userid, 1)
											H = int(es.getplayerprop(a_userid, _healthprop)) + 400
											es.setplayerprop(a_userid, _healthprop, H)
											est.give(a_userid, "weapon_m249")
							if choice == "Be Doctor":
								x,y,z = es.getplayerlocation(userid)
								es.server.cmd('est_effect 10 #a 0 sprites/laser.vmt %s %s %s -10 250 2 10 100 0 5 5 255 255 1' %(x,y,z))
								es.server.cmd('est_effect 11 #a 0 sprites/bluelaser1.vmt %s %s %s 2 8 255' %(x,y,z))
								es.server.cmd('est_effect 11 #a 0 effects/exit1.vmt %s %s %s 2 3 255' %(x,y,z))
								DEAD_LIST = []
								for a_userid in es.getUseridList():
									if not es.isbot(a_userid) and not est.isalive(a_userid):
										if es.getplayerteam(a_userid) == int(sv('humanteam')):
											DEAD_LIST.append(a_userid)
								if str(DEAD_LIST) != "[]":
									spawn_userid = random.choice(DEAD_LIST)
									est.spawn(spawn_userid)
									gamethread.delayed(0.2, est.teleport, (spawn_userid, x, y, z))
									gamethread.delayed(0.2, est.give, (spawn_userid, "weapon_mp5navy"))
							if choice == "Remote Human":
								x,y,z = es.getplayerlocation(userid)
								es.server.cmd('est_effect 10 #a 0 sprites/laser.vmt %s %s %s -10 250 2 10 100 0 5 5 255 255 1' %(x,y,z))
								es.server.cmd('est_effect 11 #a 0 sprites/bluelaser1.vmt %s %s %s 2 8 255' %(x,y,z))
								skill = int(es.keygetvalue(login_id, "player_data", "skill2"))
								for a_userid in getbot():
									if es.getplayerteam(a_userid) == int(sv('humanteam')):
										est.spawn(a_userid)
										if skill:
											gamethread.delayed(0.2, est.teleport, (a_userid, x, y, z))
								if skill: es.server.cmd('est_effect 11 #a 0 effects/exit1.vmt %s %s %s 2 3 255' %(x,y,z))
							if choice == "Remote Human2":
								x,y,z = es.getplayerlocation(userid)
								es.server.cmd('est_effect 10 #a 0 sprites/laser.vmt %s %s %s -10 250 2 10 100 0 5 5 255 255 1' %(x,y,z))
								es.server.cmd('est_effect 10 #a 0 sprites/laser.vmt %s %s %s -10 500 2 10 100 0 5 5 255 255 1' %(x,y,z))
								es.server.cmd('est_effect 11 #a 0 sprites/bluelaser1.vmt %s %s %s 2 8 255' %(x,y,z))
								es.server.cmd('est_effect 11 #a 0 effects/exit1.vmt %s %s %s 2 3 255' %(x,y,z))
								for a in playerlib.getPlayerList("#human,#dead"):
									if es.getplayerteam(a.userid) == int(sv('humanteam')):
										est.spawn(a.userid)
										gamethread.delayed(0.2, est.give, (a.userid, "weapon_m249"))
										gamethread.delayed(0.2, est.teleport, (a.userid, x, y, z))
										gamethread.delayed(0.2, es.server.cmd, ('es_xsexec %s coverme' %(userid)))
								for a in playerlib.getPlayerList("#bot"):
									if es.getplayerteam(a.userid) == int(sv('humanteam')):
										est.spawn(a.userid)
										gamethread.delayed(0.2, est.removeweapon, (a.userid, 1))
										gamethread.delayed(0.2, est.give, (a.userid, "weapon_m249"))
										gamethread.delayed(0.2, est.teleport, (a.userid, x, y, z))
										gamethread.delayed(0.2, es.server.cmd, ('es_xsexec %s coverme' %(userid)))
							if choice == "Be : Soldier(SR)":
								unlock_name = BUYMENU_LIST[choice]['need_unlock']
								if int(es.keygetvalue(login_id, "player_data", unlock_name)) > 0:
									es.keysetvalue(login_id, "player_data", "unlock_4", 0)
									es.keysetvalue(login_id, "player_data", "mastery", "용병(SR) ")
									es.server.cmd('es_xsexec %s "say 출격 준비는 되있습니다."' %(userid))
							if choice == "Be : Soldier(AR)":
								unlock_name = BUYMENU_LIST[choice]['need_unlock']
								if int(es.keygetvalue(login_id, "player_data", unlock_name)) > 0:
									es.keysetvalue(login_id, "player_data", "unlock_3", 0)
									es.keysetvalue(login_id, "player_data", "mastery", "용병(AR) ")
									es.server.cmd('es_xsexec %s "say 언제든지 싸울 준비는 되있습니다."' %(userid))
							if choice == "Web Share":
								player_count = 0
								for fuserid in getalivehuman():
									if es.getplayerteam(fuserid) > 1: player_count += 1
								player_count = int(player_count) - 1
								for fuserid in getalivehuman():
									if es.getplayerteam(fuserid) == int(sv('humanteam')):
										if fuserid != userid:
											 est.cashadd(fuserid, float(5000 / player_count))
							if choice == "Rich or Poor":
								if random.randint(1,2) == random.randint(1,3):
									esc.msg("#blue %s 유저#255,255,255는 #gold부자#255,255,255가 되었습니다!" %(username))
									est.cash(userid, "+", 10000)
								else:
									esc.msg("#blue %s 유저#255,255,255는 #125,125,125거지#255,255,255가 되었습니다!" %(username))
							if choice == "Be Nurse":
								est.play("#h", "items/smallmedkit1.wav")
								player_count = getplayercount()
								player_count = int(player_count) - 1
								be_health = 300 / player_count
								be_health = est.rounddecimal(be_health, 0)
								be_health = be_health.replace(".0", "")
								be_health = int(be_health)
								for fuserid in getalivehuman():
									if fuserid != userid:
										est.healthadd(fuserid, be_health)
							if choice == "SUIT!": est.give("#h!d", 'item_assaultsuit')
							if choice == "HE Grenade World":
								x,y,z = es.getplayerlocation(userid)
								es.server.cmd('est_effect 11 #a 0 effects/exit1.vmt %s %s %s 2 3 255' %(x,y,z))	
								delay = 0
								grenade_count = random.randint(1,30)
								while grenade_count > 0:
									grenade_count -= 1
									delay = float(delay)
									gamethread.delayed(delay, es.server.cmd, ('es_xgive %s %s' %(userid, "weapon_hegrenade")))
							if choice == "Weapon World":
								x,y,z = es.getplayerlocation(userid)
								es.server.cmd('est_effect 11 #a 0 effects/exit1.vmt %s %s %s 2 3 255' %(x,y,z))
								allprimary = ["weapon_ak47", "weapon_aug", "weapon_awp", "weapon_famas", "weapon_g3sg1", "weapon_galil", "weapon_m249", "weapon_m3", "weapon_m4a1", "weapon_mac10", "weapon_mp5navy", "weapon_p90", "weapon_scout", "weapon_sg550", "weapon_sg552", "weapon_tmp", "weapon_ump45", "weapon_xm1014"]
								allsecondary = ["weapon_deagle", "weapon_elite", "weapon_fiveseven", "weapon_glock", "weapon_p228", "weapon_usp"]
								delay = 0
								for a in allprimary:
									delay = float(delay) + 0.1
									gamethread.delayed(delay, es.server.cmd, ('es_xgive %s %s' %(userid, a)))
								for a in allsecondary:
									delay = float(delay) + 0.1
									gamethread.delayed(delay, es.server.cmd, ('es_xgive %s %s' %(userid, a)))
							if choice == "Be Nurse EX":
								est.play("#h", "items/smallmedkit1.wav")
								player_count = 0
								for a in playerlib.getPlayerList("#human"):
									if es.getplayerteam(a.userid) > 1 and est.isalive(a.userid): player_count += 1
								player_count = int(player_count) - 1
								be_health = 600 / player_count
								be_health = est.rounddecimal(be_health, 0)
								be_health = be_health.replace(".0", "")
								be_health = int(be_health)
								for a in playerlib.getPlayerList("#human"):
									if es.getplayerteam(a.userid) == int(sv('humanteam')):
										if a.userid != userid:
											keymath("buymenu", a.userid, "health", "+", be_health)
											est.healthadd(a.userid, be_health)
							if choice == "Speed + 0.01":
								speedadd(userid, 0.01)
								es.playsound(userid, "items/smallmedkit1.wav", 1.0)
								_speed = float(es.keygetvalue("buymenu", userid, "speed")) + float(0.01)
								es.keysetvalue("buymenu", userid, "speed", _speed)
							if choice == "Speed + 0.05":
								speedadd(userid, 0.05)
								es.playsound(userid, "items/smallmedkit1.wav", 1.0)
								_speed = float(es.keygetvalue("buymenu", userid, "speed")) + float(0.05)
								es.keysetvalue("buymenu", userid, "speed", _speed)
					else: esc.tell(userid, "레벨이 부족합니다.")
				else: esc.tell(userid, "MP가 모자랍니다.")
			else: esc.tell(userid, "MP가 모자랍니다.")
		else: esc.tell(userid, "달러가 모자랍니다.")

def sayFilter(userid, text, teamonly):
	if es.isbot(userid):
		username = es.getplayername(userid)
		if username == "[Unknown] .": return (userid, text, teamonly)
		if username == "[Unknown] ?": return (userid, text, teamonly)
	if userid > 1 and sayok[userid] == 1:
		sayok[userid] = 0
		gamethread.delayed(0.5, sayok_block, (userid))
		login_id = getplayerid(userid)
		username = es.getplayername(userid)
		username = username.replace('"', '')
		steamid = es.getplayersteamid(userid)
		team = int(es.getplayerprop(userid, "CBaseEntity.m_iTeamNum"))
		rawtext = text.replace('"', "")
		rawtext = rawtext.replace("#", "＃")
		rawtext = rawtext.replace("", "")
		rawtext = rawtext.replace("", "")
		rawtext = rawtext.replace("\\", "/")
		rawtext = rawtext.replace("->", "→")
		rawtext = rawtext.replace("<-", "←")
		rawtext_args = rawtext.split()
		msgok = 1
		if "!login" in rawtext:
			esc.tell(userid, "#255,255,255콘솔입니다. 채팅창에 입력하면 안됩니다!")
			msgok = 0
		if "!register" in rawtext:
			esc.tell(userid, "#255,255,255콘솔입니다. 채팅창에 입력하면 안됩니다!")
			msgok = 0
		if "!find_id" in rawtext:
			esc.tell(userid, "#255,255,255콘솔입니다. 채팅창에 입력하면 안됩니다!")
			msgok = 0
		if "!answer_id" in rawtext:
			esc.tell(userid, "#255,255,255콘솔입니다. 채팅창에 입력하면 안됩니다!")
			msgok = 0
		if msgok == 1:
			level = es.keygetvalue(login_id, "player_data", "level")
			mastery = es.keygetvalue(login_id, "player_data", "mastery")
			mastery = mastery.replace("흡혈귀 ", "#255,0,0흡혈귀 ")
			mastery = mastery.replace("스칼렛 ", "#150,0,0스칼렛 ")
			mastery = mastery.replace("무 ", "#0,0,0無 ")
			mastery = mastery.replace("용병(AR) ", "#0,100,0용병(AR) ")
			mastery = mastery.replace("용병(SR) ", "#100,50,0용병(SR) ")
			mastery = mastery.replace("Juggernut ", "#0,100,0Jugger#100,50,0nut ")
			mastery = mastery.replace("탐험가 ", "#0,75,0탐험#125,125,0가 ")
			mastery = mastery.replace("의사 ", "#255,255,255의사 ")
			mastery = mastery.replace("프린세스 ", "#pink프린세스 ")
			mastery = mastery.replace("과학자 ", "#255,255,255과학자 ")
			mastery = mastery.replace("수학자 ", "#255,255,255수학자 ")
			mastery = mastery.replace("무녀 ", "#green무녀 ")
			mastery = mastery.replace("암살자 ", "#0,0,0암살자 ")
			mastery = mastery.replace("샷거너 ", "#55,55,55샷거너 ")
			mastery = mastery.replace("피스톨 슈터 ", "#55,55,55피스톨 슈터 ")
			mastery = mastery.replace("봄버맨 ", "#255,0,0봄#0,0,0버맨 ")
			mastery = mastery.replace("요괴 ", "#255,0,0요괴 ")
			mastery = mastery.replace("도박사 ", "#gold도박사 ")
			mastery = mastery.replace("피실험체 ", "#255,0,0피실험체 ")
			mastery = mastery.replace("아이언 맨 ", "#white아이언 맨 ")
			if level != None:
				if int(es.keygetvalue(login_id, "player_data", "supporter_time")) > 0:
					levelcolor = "0,255,255"
					if int(es.keygetvalue(login_id, "player_data", "supporter_time")) > (604800*2):
						levelcolor = "255,255,0"
					if str(login_id) == str(sv('support_ranker_1')):
						levelcolor = "0,0,0"
				else: levelcolor = "0,255,0"
			else: levelcolor = "0,255,0"
			if int(team) <= 1: teamcolor = "white"
			if int(team) == 2: teamcolor = "red"
			if int(team) == 3: teamcolor = "blue"
			if int(es.keygetvalue(login_id, "player_data", "supporter_time")) > (604800*2): teamcolor = "0,255,255"
			if str(login_id) == str(sv('support_ranker_1')): teamcolor = "purple"
			esc.msg("%s#%s[Lv.%s]#%s %s :#default %s" %(mastery, levelcolor, level, teamcolor, username, rawtext))
			if rawtext == "!메뉴":
				rpgmenu.send(userid)
			if rawtext == "!프로젝트3 접속":
				abcd = 1
			if rawtext == "!초기화(경고없음)":
				st = getplayerid(userid)
				reset_player(st)
			if rawtext == "!정보":
				if not est.isalive(userid):
					target = int(es.getplayerprop(userid, "CCSPlayer.baseclass.m_hObserverTarget"))
					target_userid = getuseridfromhandle(target)
					if not es.isbot(target_userid):
						target_id = getplayerid(target_userid)
						est.motd_w(userid, "None", ",", "http://boksu.crplab.kr/zeisen/bot/%s.html" %(target_username))
					if es.isbot(target_userid):
						target_username = es.getplayername(target_userid)
						target_username = target_username.replace(" ", "_")
						target_username = target_username.lower()
						if "[normal]" in target_username: target_username = "[normal]"
						if "[shooter]" in target_username: target_username = "[shooter]"
						est.motd_w(userid, "None", ",", "http://boksu.crplab.kr/zeisen/bot/%s.html" %(target_username))
			if rawtext in "motd, !motd":
				est.motd_w(userid, "None", ".", "http://boksu.crplab.kr/zeisen/motd.html")
				#es.server.cmd('es_xsexec %s motd' %(userid))
			if rawtext == "!건의":
				est.motd_w(userid, "None", ".", "steamcommunity.com/groups/zephma#announcements/detail/1405428542812811194")
			if rawtext == "!서포터":
				est.motd_w(userid, "Supporter", ".", "steamcommunity.com/groups/zephma/discussions/0/558751813286346842/")
			if rawtext == "!도박 주사위":
				esc.msg("#255,255,255결과 : %s" %(random.randint(1,6)))
			if rawtext == "!월드 (노말)":
				listpopup = popuplib.easylist('listpopup', NORMAL_WORLD)
				listpopup.settitle("＠ List")
				listpopup.send(userid)
				popuplib.delete('listpopup')
			if rawtext == "!월드 (페어리)":
				listpopup = popuplib.easylist('listpopup', FAIRY_WORLD)
				listpopup.settitle("＠ List")
				listpopup.send(userid)
				popuplib.delete('listpopup')
			if rawtext == "!월드 (몬스터)":
				listpopup = popuplib.easylist('listpopup', MONSTER_WORLD)
				listpopup.settitle("＠ List")
				listpopup.send(userid)
				popuplib.delete('listpopup')
			if int(sv('say_block')) == 0:
				if rawtext == "!도박 777":
					if est.isalive(userid):
						es.set("say_block", 1)
						es.server.cmd('es_xdelayed 3 es_xset say_block 0')
						z = random.choice(["7", "바나나", "바나나", "포도", "포도", "포도", "사과", "사과", "사과", "사과"])
						x = random.choice(["7", "바나나", "바나나", "포도", "포도", "포도", "사과", "사과", "사과", "사과"])
						c = random.choice(["7", "바나나", "바나나", "포도", "포도", "포도", "사과", "사과", "사과", "사과"])
						usermsg.hudhint(userid, "확률 : 사과 > 포도 > 바나나 > 7")
						gamethread.delayed(1, esc.msg, ("#255,255,255결과 : %s" %(z)))
						gamethread.delayed(2, esc.msg, ("#255,255,255결과 : %s" %(x)))
						gamethread.delayed(3, esc.msg, ("#255,255,255결과 : %s" %(c)))
				if rawtext == "!도박 러시안 룰렛 10%":
					if est.isalive(userid):
						es.set("say_block", 1)
						es.server.cmd('es_xdelayed 5 es_xset say_block 0')
						esc.msg("#255,255,255 %s님이 도박을 시도합니다..." %(username))
						est.play("#h", "weapons/deagle/de_clipin.wav")
						est.play("#h", "weapons/deagle/de_clipin.wav")
						est.play("#h", "weapons/deagle/de_clipin.wav")
						random_max = 10
						if random.randint(1,random_max) == 1:
							gamethread.delayed(5, est.slay, (userid))
							gamethread.delayed(5, est.play, ("#h", "weapons/deagle/deagle-1.wav"))
						else:
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
				if rawtext == "!도박 러시안 룰렛 25%":
					if est.isalive(userid):
						es.set("say_block", 1)
						es.server.cmd('es_xdelayed 5 es_xset say_block 0')
						esc.msg("#255,255,255 %s님이 도박을 시도합니다..." %(username))
						est.play("#h", "weapons/deagle/de_clipin.wav")
						est.play("#h", "weapons/deagle/de_clipin.wav")
						est.play("#h", "weapons/deagle/de_clipin.wav")
						random_max = 4
						if random.randint(1,random_max) == 1:
							gamethread.delayed(5, est.slay, (userid))
							gamethread.delayed(5, est.play, ("#h", "weapons/deagle/deagle-1.wav"))
						else:
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
				if rawtext == "!도박 러시안 룰렛 50%":
					if est.isalive(userid):
						es.set("say_block", 1)
						es.server.cmd('es_xdelayed 5 es_xset say_block 0')
						esc.msg("#255,255,255 %s님이 도박을 시도합니다..." %(username))
						est.play("#h", "weapons/deagle/de_clipin.wav")
						est.play("#h", "weapons/deagle/de_clipin.wav")
						est.play("#h", "weapons/deagle/de_clipin.wav")
						random_max = 2
						if random.randint(1,random_max) == 1:
							gamethread.delayed(5, est.slay, (userid))
							gamethread.delayed(5, est.play, ("#h", "weapons/deagle/deagle-1.wav"))
						else:
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
				if rawtext == "!도박 로켓 룰렛 10%":
					if est.isalive(userid):
						es.set("say_block", 1)
						es.server.cmd('es_xdelayed 5 es_xset say_block 0')
						esc.msg("#255,255,255 %s님이 도박을 시도합니다..." %(username))
						est.play("#h", "weapons/deagle/de_clipin.wav")
						est.play("#h", "weapons/deagle/de_clipin.wav")
						est.play("#h", "weapons/deagle/de_clipin.wav")
						random_max = 10
						if random.randint(1,random_max) == 1:
							gamethread.delayed(5, est.rocket, (userid))
							gamethread.delayed(5, est.play, ("#h", "weapons/deagle/deagle-1.wav"))
						else:
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
				if rawtext == "!도박 로켓 룰렛 25%":
					if est.isalive(userid):
						es.set("say_block", 1)
						es.server.cmd('es_xdelayed 5 es_xset say_block 0')
						esc.msg("#255,255,255 %s님이 도박을 시도합니다..." %(username))
						est.play("#h", "weapons/deagle/de_clipin.wav")
						est.play("#h", "weapons/deagle/de_clipin.wav")
						est.play("#h", "weapons/deagle/de_clipin.wav")
						random_max = 4
						if random.randint(1,random_max) == 1:
							gamethread.delayed(5, est.rocket, (userid))
							gamethread.delayed(5, est.play, ("#h", "weapons/deagle/deagle-1.wav"))
						else:
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
				if rawtext == "!도박 로켓 룰렛 50%":
					if est.isalive(userid):
						es.set("say_block", 1)
						es.server.cmd('es_xdelayed 5 es_xset say_block 0')
						esc.msg("#255,255,255 %s님이 도박을 시도합니다..." %(username))
						est.play("#h", "weapons/deagle/de_clipin.wav")
						est.play("#h", "weapons/deagle/de_clipin.wav")
						est.play("#h", "weapons/deagle/de_clipin.wav")
						random_max = 2
						if random.randint(1,random_max) == 1:
							gamethread.delayed(5, est.rocket, (userid))
							gamethread.delayed(5, est.play, ("#h", "weapons/deagle/deagle-1.wav"))
						else:
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
							gamethread.delayed(5, est.play, ("#h", "weapons/clipempty_pistol.wav"))
			if rawtext == "!레벨랭킹":
				if int(es.keygetvalue(login_id, "player_data", "supporter_time")) > 0:
					level_rank.send(userid)
				else: esc.tell(userid, "당신은 서포터가 아닙니다.")
			if rawtext == "!언락":
				unlock_p.send(userid)
			if int(level) != 1:
				if rawtext_args[0] == "!거래":
					wg_id = int(rawtext_args[1])
					keyname = ITEM_LIST[int(rawtext_args[2])]['name']
					much = int(rawtext_args[3])
					if int(es.keygetvalue(login_id, "player_data", keyname)) >= much and much > 0:
						trade_enable = ITEM_LIST[int(rawtext_args[2])]['trade']
						if trade_enable:
							check = es.getplayerhandle(wg_id)
							if check > 0 and not es.isbot(wg_id):
								esc.msg("#blue %s 유저#255,255,255가#blue %s 유저#255,255,255에게#gold %s 아이템#255,255,255을#gold %s#255,255,255개 만큼 주었습니다." %(es.getplayername(userid), es.getplayername(wg_id), ITEM_LIST[int(rawtext_args[2])]['showname'], much))
								wg_steamid = getplayerid(wg_id)
								keymath(login_id, "player_data", keyname, '-', much)
								keymath(wg_steamid, "player_data", keyname, '+', much)
						else: esc.tell(userid, "#255,255,255＊ 이 아이템은 거래가 불가능합니다.")
			if rawtext == "!언락" or rawtext == "!unlock":
				unlock_popup = popuplib.easymenu('unlock_%s' %(userid), None, none_select)
				for a in UNLOCK_LIST:
					state = 0
					if int(es.keygetvalue(login_id, "player_data", UNLOCK_LIST[a]['unlock'])) > 0: state = 1
					unlock_popup.addoption(a, "[Solo] %s : %s" %(a, UNLOCK_LIST[a]['unlock_info']), state)
			#if rawtext == "!revote": es.server.cmd('es_xsexec %s sm_revote' %(userid))
			if str(sv('sv_password')) == "" and themap() == "de_nightfever":
				if rawtext_args[0] == "!invite":
					in_id = int(rawtext_args[1])
					if es.getplayerhandle(in_id) > 0 and est.isalive(in_id):
						if userid != in_id:
							x,y,z = es.getplayerlocation(userid)
							zozo = popuplib.easymenu('invite_%s' %(userid), None, invite_select)
							zozo.settitle("＠ %s 님이 당신을 초대했습니다!" %(username))
							zozo.addoption("teleport %s %s %s" %(x,y,z), "승락한다.")
							zozo.send(in_id)
							popuplib.delete('invite_%s' %(userid))
			if rawtext == "!리스트":
				SHOW_LIST = []
				for a_userid in gethuman():
					name = es.getplayername(a_userid)
					name = name.replace('"', '')
					name_format = "[%s] %s" %(a_userid, name)
					SHOW_LIST.append(name_format)
					esc.tell(userid, "#255,255,255[%s]#blue %s" %(a_userid, name))
				listpopup = popuplib.easylist('listpopup', SHOW_LIST)
				listpopup.settitle("＠ List")
				listpopup.send(userid)
				popuplib.delete('listpopup')
			if rawtext == "!랭킹 (엔)":
				rank_money_setting()
				ranking_m_popup.send(userid)
			if rawtext == "!랭킹 (시간)":
				rank_p_setting()
				ranking_p_popup.send(userid)
			if rawtext == "!랭킹 (서포트)":
				rank_support_setting()
				ranking_s_popup.send(userid)
			if rawtext == "!랭킹 (레벨)":
				rank_level_setting()
				ranking_level_popup.send(userid)
			if rawtext == "!세이브" or rawtext == "!save":
				esc.tell(userid, "#255,255,255세이브 되었습니다.")
				rank_money_add(userid)
				rank_level_add(userid)
				rank_support_add(userid)
				rank_p_add(userid)
				login_id = getplayerid(userid)
				es.keygroupsave(login_id, "|bot/player_data")
			if int(es.keygetvalue(login_id, "player_data", "supporter_time")) > 0:
				rank_support_add(userid)
				if rawtext.lower() == "nnosir": es.server.cmd('es_xsoon r_sendvoice %s bot/nnno_sir.wav' %(userid))
				if rawtext.lower() == "nosir": es.server.cmd('es_xsoon r_sendvoice %s bot/no_sir.wav' %(userid))
				if rawtext.lower() == "na": es.server.cmd('es_xsoon r_sendvoice %s bot/naa.wav' %(userid))
				if rawtext.lower() == "ok" or rawtext == "ㅇㅋ": es.server.cmd('es_xsoon r_sendvoice %s bot/ok.wav' %(userid))
				if rawtext.lower() == "noo": es.server.cmd('es_xsoon r_sendvoice %s bot/noo.wav' %(userid))
				if rawtext.lower() == "wow": es.server.cmd('es_xsoon r_sendvoice %s bot/whoo.wav' %(userid))
				if rawtext.lower() == "hey": es.server.cmd('es_xsoon r_sendvoice %s bot/hey.wav' %(userid))
				if rawtext.lower() == "yes": es.server.cmd('es_xsoon r_sendvoice %s bot/yesss2.wav' %(userid))
				if rawtext.lower() == "oh" or rawtext == "오": es.server.cmd('es_xsoon r_sendvoice %s bot/oh.wav' %(userid))
				if rawtext.lower() == "yea": es.server.cmd('es_xsoon r_sendvoice %s bot/yea_baby.wav' %(userid))
				if rawtext.lower() == "ohno" or rawtext == "ㅇㄴ": es.server.cmd('es_xsoon r_sendvoice %s bot/oh_no.wav' %(userid))
				if rawtext.lower() == "ohmygod": es.server.cmd('es_xsoon r_sendvoice %s bot/oh_my_god.wav' %(userid))
				if rawtext.lower() == "thisismyhouse" or rawtext == "여긴내집이야": es.server.cmd('es_xsoon r_sendvoice %s bot/this_is_my_house.wav' %(userid))
				if rawtext == "ㄴ" or rawtext.lower() == "no": es.server.cmd('es_xsoon r_sendvoice %s bot/no.wav' %(userid))
				if rawtext == "ㄴㄴㄴㄴㄴ":
					es.server.cmd('es_xsoon r_sendvoice %s bot/no.wav' %(userid))
					es.server.cmd('es_xdelayed 0.1 est_play #h bot/no.wav')
					es.server.cmd('es_xdelayed 0.2 est_play #h bot/no.wav')
					es.server.cmd('es_xdelayed 0.3 est_play #h bot/no.wav')
					es.server.cmd('es_xdelayed 0.4 est_play #h bot/no.wav')
				if rawtext == "나이스" or rawtext.lower() == "nice": es.server.cmd('es_xsoon r_sendvoice %s bot/nice.wav' %(userid))
				if rawtext == "음": es.server.cmd('es_xsoon r_sendvoice %s zeisenproject_-1/autosounds/saysounds/n-.mp3' %(userid))
				if rawtext == "앙?" or rawtext.lower() == "ang?": es.server.cmd('es_xsoon r_sendvoice %s zeisenproject_-1/autosounds/gay/ang.mp3' %(userid))
				if rawtext == "오마이숄더": es.server.cmd('es_xsoon r_sendvoice %s zeisenproject_-1/autosounds/gay/ohmy.mp3' %(userid))
				if rawtext == "ㅗ" or rawtext == "fuckyou": es.server.cmd('es_xsoon r_sendvoice %s zeisenproject_-1/autosounds/gay/fuckyou.mp3' %(userid))
				if rawtext == "네!": es.server.cmd('es_xsoon r_sendvoice %s zeisenproject_-1/autosounds/cirno_follow.mp3' %(userid))
				if rawtext == "란란루": es.server.cmd('es_xsoon r_sendvoice %s zeisenproject_-1/autosounds/saysounds/ranranru.mp3' %(userid))
				if rawtext == "진입하라": es.server.cmd('es_xsoon r_sendvoice %s zeisenproject_-1/autosounds/saysounds/combinesound/movein.wav' %(userid))
				if rawtext == "움직여": es.server.cmd('es_xsoon r_sendvoice %s zeisenproject_-1/autosounds/saysounds/combinesound/moveit2.wav' %(userid))
				if rawtext == "동작그만": es.server.cmd('es_xsoon r_sendvoice %s zeisenproject_-1/autosounds/saysounds/combinesound/dontmove.wav' %(userid))
				if rawtext == "저 캔을 집어라": es.server.cmd('es_xsoon r_sendvoice %s zeisenproject_-1/autosounds/saysounds/combinesound/pickupthecan1.wav' %(userid))
				if rawtext == "저 캔을 집으라고 했다": es.server.cmd('es_xsoon r_sendvoice %s zeisenproject_-1/autosounds/saysounds/combinesound/pickupthecan3.wav' %(userid))
				if rawtext == "첫번째 경고다 비켜라": es.server.cmd('es_xsoon r_sendvoice %s zeisenproject_-1/autosounds/saysounds/combinesound/firstwarningmove.wav' %(userid))
				if rawtext == "알았다": es.server.cmd('es_xsoon r_sendvoice %s zeisenproject_-1/autosounds/saysounds/combinesound/affirmative.wav' %(userid))
				if rawtext == "숙여": es.server.cmd('es_xsoon r_sendvoice %s zeisenproject_-1/autosounds/saysounds/combinesound/getdown.wav' %(userid))
				if rawtext == "좋아 가도 좋다": es.server.cmd('es_xsoon r_sendvoice %s zeisenproject_-1/autosounds/saysounds/combinesound/allrightyoucango.wav' %(userid))
				if rawtext == "ㅋㅋㅋ": es.server.cmd('es_xsoon r_sendvoice %s zeisenproject_-1/autosounds/saysounds/combinesound/chuckle.wav' %(userid))
			if rawtext == "rocket" or rawtext == "!rocket" or rawtext == "!로켓":
				player = playerlib.getPlayer(userid)
				if player.onGround() == 1:
					if int(sv('round')) <= 7:
						est.rocket(userid)
			if rawtext_args[0] == "!volume" or rawtext_args[0] == "!볼륨":
				if len(rawtext_args) == 2:
					volume = float(rawtext_args[1])
					es.keysetvalue("total_players", steamid, "volume", volume)
					esc.tell(userid, "#255,255,255볼륨 설정 완료 (%s％)" %(volume * 100))
			if rawtext == "!옵션" or rawtext == "!option":
				register_id = es.keygetvalue("total_players", steamid, "register_id")
				automatic_id = es.keygetvalue("total_players", steamid, "automatic_id")
				automatic_password = es.keygetvalue("total_players", steamid, "automatic_password")
				volume = float(es.keygetvalue("total_players", steamid, "volume"))
				option_popup = popuplib.easymenu('option_%s' %(userid), None, none_select)
				option_popup.addoption(0, "당신이 만든 계정 : %s" %(register_id), 0)
				option_popup.addoption(0, "오토 로그인 계정 : %s" %(automatic_id), 0)
				option_popup.addoption(0, "오토 로그인 패스워드 : %s" %(automatic_password), 0)
				option_popup.addoption(0, "볼륨 : %s" %(volume), 0)
				if int(es.keygetvalue(login_id, "player_data", "supporter_time")) > 0:
					jump_count = es.keygetvalue(login_id, "player_data", "jump_count")
					option_popup.addoption(0, "점프 횟수 : %s회" %(jump_count))
				option_popup.send(userid)
				popuplib.delete('option_%s' %(userid))
			return (0, 0, 0)
	else:
		if userid > 1: esc.tell(userid, "#255,255,255천천히 말하세요, 0.5초 딜레이가 있습니다.")
		return (0, 0, 0)

def effectsound(music):
	for a_userid in gethuman():
		es.playsound(a_userid, music, 1.0)

def invite_select(userid, choice, popupname):
	choice_args = choice.split()
	if "teleport" in choice:
		es.setpos(userid, choice_args[1], choice_args[2], choice_args[3])

def getdistance(userid, attacker):
	victim_location = vecmath.vector(es.getplayerlocation(userid))
	attacker_location = vecmath.vector(es.getplayerlocation(attacker))
	return vecmath.distance(victim_location, attacker_location) * 0.0254

def sayok_block(userid):
	sayok[userid] = 1

def npc_select(userid, choice, popupname):
	if popupname == "sonic_npc":
		choice_args = choice.split()

def npc_tell(userid, name, text):
	esc.tell(userid, " %s :#default %s" %(name, text))

def npc_msg(name, text):
	esc.msg(" %s :#default %s" %(name, text))

def speedadd(userid, value):
	_sfpeed = float(es.getplayerprop(userid, "CBasePlayer.localdata.m_flLaggedMovementValue")) + float(value)
	es.setplayerprop(userid, "CBasePlayer.localdata.m_flLaggedMovementValue", _sfpeed)

def getentitycolor(userid):
        color = es.getindexprop(userid, "CBaseEntity.m_clrRender")
        return tuple(int(x) for x in (color & 0xff, (color & 0xff00) >> 8, (color & 0xff0000) >> 16, (color & 0xff000000) >> 24))

def getplayercolor(userid):
        color = es.getplayerprop(userid, "CBaseEntity.m_clrRender")
        return tuple(int(x) for x in (color & 0xff, (color & 0xff00) >> 8, (color & 0xff0000) >> 16, (color & 0xff000000) >> 24))

def getplayerid(userid):
	steamid = es.getplayersteamid(userid)
	steamid = steamid.replace("STEAM", "")
	steamid = steamid.replace(":", "")
	steamid = steamid.replace("_", "")
	return steamid

def getmodelname(index):
	ptr = spe.getEntityOfIndex(index)
	if not ptr:
		return None 
	return ctypes.string_at(spe.getLocVal('i', ptr + OFFSET_MODEL_NAME))

def givehat(userid, r, g, b, a):
        eyeangle = vecmath.vector(playerlib.getPlayer(userid).getViewAngle())
        eyeangle.x -= 10
        eyeangle.y -= 180
        index = es.createentity("prop_dynamic_override")
	total_name = "hat_%s" %(userid)
        es.setentityname(index, total_name)
        location = es.getplayerlocation(userid)
	est.setentmodel(index, 'models/props_combine/breentp_rings.mdl')
        es.entitysetvalue(index, "origin", '%s %s %s'%(location[0] - .5, location[1], location[2] + 60))
        es.entitysetvalue(index, "solid", 1)
        es.entitysetvalue(index, "angles", eyeangle.getstr(" "))
        es.setindexprop(index, 'CBaseEntity.m_hOwnerEntity', es.getplayerhandle(userid))
        es.server.queuecmd("es_xspawnentity %s"% index)
	es.entitysetvalue(index, 'DefaultAnim', 'idle')
        es.server.queuecmd("es_xfire %s %s %s !activator"% (userid, total_name, 'SetParent'))
	est.setentitycolor(index, r, g, b, a)

def themap():
	return str(sv('eventscripts_currentmap'))

def svmath(_variable, A, value):
	B = int(sv(_variable))
	if A == "+": B += value
	if A == "-": B -= value
	if A == "*": B *= value
	if A == "/": B = B / value
	es.set(_variable, B)
	return B

def getplayercount():
        count = 0
        for userid in es.getUseridList():
                if es.getplayerteam(userid) > 1: count += 1
	return count

def exist_setv(_variable, value):
	check = es.exists("variable", _variable)
	if not check:
		es.set(_variable, value)

def setClanTag(userid, clan_tag):
	length = len(clan_tag)
	if length >= MAX_SIZE:
		raise ValueError('Clan tag is too long')
	es.server.cmd('r_getclantag %s "%s"' %(userid, clan_tag))

def getClanTag(userid):
	es.set("getvv", 0)
	es.server.cmd('r_getclantag getvv %s' %(userid))
	getvv = str(sv('getvv'))
	return getvv

def break_door():
	playsound("doors/latchlocked2.wav")
	gamethread.delayed(1, est.play, ("#h", "doors/latchlocked2.wav"))
	gamethread.delayed(2, est.play, ("#h", "doors/latchlocked2.wav"))
	gamethread.delayed(3, est.play, ("#h", "doors/latchlocked2.wav"))
	gamethread.delayed(4, est.play, ("#h", "doors/latchlocked2.wav"))
	gamethread.delayed(5, est.play, ("#h", "doors/latchlocked2.wav"))
	gamethread.delayed(8, est.play, ("#h", "doors/heavy_metal_stop1.wav"))
	gamethread.delayed(10, est.play, ("#h", "doors/heavy_metal_stop1.wav"))
	gamethread.delayed(12, est.play, ("#h", "doors/heavy_metal_stop1.wav"))
	gamethread.delayed(15, est.play, ("#h", "doors/heavy_metal_stop1.wav"))
	gamethread.delayed(18, est.play, ("#h", "doors/heavy_metal_stop1.wav"))
	gamethread.delayed(19, est.play, ("#h", "doors/heavy_metal_stop1.wav"))
	gamethread.delayed(20, est.play, ("#h", "doors/heavy_metal_stop1.wav"))
	gamethread.delayed(21, est.play, ("#h", "doors/heavy_metal_stop1.wav"))
	gamethread.delayed(22, est.play, ("#h", "doors/heavy_metal_stop1.wav"))
	gamethread.delayed(22.8, est.play, ("#h", "doors/heavy_metal_stop1.wav"))
	gamethread.delayed(23, est.play, ("#h", "doors/heavy_metal_stop1.wav"))
	gamethread.delayed(23.3, est.play, ("#h", "doors/heavy_metal_stop1.wav"))
	gamethread.delayed(24, est.play, ("#h", "doors/heavy_metal_stop1.wav"))
	gamethread.delayed(30, est.play, ("#h", "doors/latchunlocked1.wav"))
	gamethread.delayed(30, est.play, ("#h", "doors/latchunlocked1.wav"))
	gamethread.delayed(30, est.play, ("#h", "doors/latchunlocked1.wav"))
	gamethread.delayed(30, est.play, ("#h", "doors/latchunlocked1.wav"))

def keymath(keygroup, steamid, value, what, much):
	if what == "+":
		A = int(es.keygetvalue(keygroup, steamid, value)) + int(much)
		if value == "jump_count":
			if A == 10000:
				login_id = keygroup
				userid = useridfromloginid(login_id)
				es.keysetvalue(login_id, "player_data", "unlock_1", 1)
				es.server.cmd('r_unlock %s "Jump! Jump! Jump!"' %(userid))
				esc.tell(userid, "#gold[Unlocked Skill] Jumper")
	if what == "-":
		A = int(es.keygetvalue(keygroup, steamid, value)) - int(much)
	if what == "*":
		A = int(es.keygetvalue(keygroup, steamid, value)) * int(much)
	if what == "/":
		A = int(es.keygetvalue(keygroup, steamid, value)) / int(much)
	es.keysetvalue(keygroup, steamid, value, A)
	return A


def ttt():
	x,y,z = es.getplayerlocation(9)
	for a in playerlib.getPlayerList("#bot,#alive"):
		bot_move(a.userid, x, y, z, "FASTEST_ROUTE")

def story_warning():
	est.play("#h", "zeisenproject_-1/autosounds/story_sounds/wsound_4.wav")
	#esc.msg("#255,0,0※ Warning\n \n본 스토리는 정신건강에 좋지 않은 내용을 포함하고 있습니다.\n심장이 약하시거나 예민하신 분들은 플레이를 삼가해주세요.")
	for a_userid in gethuman():
		usermsg.hudmsg(a_userid, "※ Warning\n \n본 스토리는 정신건강에 좋지 않은 내용을 포함하고 있습니다.\n심장이 약하시거나 예민하신 분들은 플레이를 삼가해주세요.", 0, 0.25, 0.25, 255, 0, 0)
		gamethread.delayed(1, usermsg.hudmsg, (a_userid, "※ Warning\n \n본 스토리는 정신건강에 좋지 않은 내용을 포함하고 있습니다.\n심장이 약하시거나 예민하신 분들은 플레이를 삼가해주세요.", 1, 0.25, 0.25, 255, 0, 0))
		gamethread.delayed(2, usermsg.hudmsg, (a_userid, "※ Warning\n \n본 스토리는 정신건강에 좋지 않은 내용을 포함하고 있습니다.\n심장이 약하시거나 예민하신 분들은 플레이를 삼가해주세요.", 2, 0.25, 0.25, 255, 0, 0))
		gamethread.delayed(3, usermsg.hudmsg, (a_userid, "※ Warning\n \n본 스토리는 정신건강에 좋지 않은 내용을 포함하고 있습니다.\n심장이 약하시거나 예민하신 분들은 플레이를 삼가해주세요.", 3, 0.25, 0.25, 255, 0, 0))

def bot_move(userid, x, y, z, route="SAFEST_ROUTE"):
	loc = (x, y, z)
	#vec_ptr = createVector(*loc)
	#spe.call('MoveTo', spe.getPlayer(userid), vec_ptr, route)
	#spe.dealloc(vec_ptr)

def createVector(x, y, z):
	ptr = spe.alloc(12)
	spe.setLocVal('f', ptr + 0, x)
	spe.setLocVal('f', ptr + 4, y)
	spe.setLocVal('f', ptr + 8, z)
	return ptr

def isdead(userid):
        return est.isalive(userid)

def onGround(userid):
	return es.getplayerprop(userid, 'CBasePlayer.m_fFlags') & 1

def rain():
	trrr = random.randint(1,4)
	est.play("#h", "ambient/atmosphere/thunder%s.wav" %(trrr))
	est.play("#h", "ambient/water/water_flow_loop1.wav", 9999999, 0.25)
	index = es.createentity("func_precipitation")
	es.entitysetvalue(index, "model", "maps/%s.bsp" % themap())
	es.entitysetvalue(index, "preciptype", 0)
	es.server.insertcmd("es_xspawnentity %i" % index)
	m_WorldMins = vecmath.Vector(es.getindexprop(0, "CWorld.m_WorldMins"))
	m_WorldMaxs = vecmath.Vector(es.getindexprop(0, "CWorld.m_WorldMaxs"))
	es.server.insertcmd("es_xsetindexprop %i CBaseEntity.m_Collision.m_vecMins %s" % (index, m_WorldMins))
	es.server.insertcmd("es_xsetindexprop %i CBaseEntity.m_Collision.m_vecMaxs %s" % (index, m_WorldMaxs))
	m_vecOrigin = (m_WorldMins + m_WorldMaxs) / 2
	es.server.insertcmd('es_xentitysetvalue %i origin "%f %f %f"' % (index, m_vecOrigin.x, m_vecOrigin.y, m_vecOrigin.z))
def thunder():
	trrr = random.randint(1,4)
	est.play("#h", "ambient/atmosphere/thunder%s.wav" %(trrr))

def snow():
	index = es.createentity("func_precipitation")
	es.entitysetvalue(index, "model", "maps/%s.bsp" % themap())
	es.entitysetvalue(index, "preciptype", 3)
	es.server.insertcmd("es_xspawnentity %i" % index)
	m_WorldMins = vecmath.Vector(es.getindexprop(0, "CWorld.m_WorldMins"))
	m_WorldMaxs = vecmath.Vector(es.getindexprop(0, "CWorld.m_WorldMaxs"))
	es.server.insertcmd("es_xsetindexprop %i CBaseEntity.m_Collision.m_vecMins %s" % (index, m_WorldMins))
	es.server.insertcmd("es_xsetindexprop %i CBaseEntity.m_Collision.m_vecMaxs %s" % (index, m_WorldMaxs))
	m_vecOrigin = (m_WorldMins + m_WorldMaxs) / 2
	es.server.insertcmd('es_xentitysetvalue %i origin "%f %f %f"' % (index, m_vecOrigin.x, m_vecOrigin.y, m_vecOrigin.z))

def useridfromloginid(loginid):
	for userid in es.getUseridList():
		userid_login_id = getplayerid(userid)
		if str(userid_login_id) == str(loginid): return userid

def npc_horrornightfever():
	create_npc('error.mdl', 'npc_horror1_nightfever', 0, 1026.4921875, 1925.50268555, 32.03125, 255, 0, 0, 255, 145.218994141)
	create_npc('error.mdl', 'npc_horror2_nightfever', 0, 565.158447266, 1915.06933594, 32.03125, 0, 0, 255, 255, 65.1191139221)
def npc_rush_v2():
	#es.entitysetvalue(index, "origin", "3369 -5414 300")
	#es.entitysetvalue(index, "classname", "npc_prop1_rush")
	#es.spawnentity(index)
	#es.setindexprop(index, "CDynamicProp.baseclass.baseclass.baseclass.m_angRotation", "0,0,0")
	create_npc('player/ct_sas', 'npc_teleport_rush1 3369 -5414 325', 1, 2157.18774414, -4093.20239258, 40.03125, 255, 255, 255, 255, 145)

def npc_nightfever():
	create_npc('player/lockcha/lockcha11/glados.mdl', 'npc_custom_nightfever', 1, -965.450744629, 2223.12670898, 16.03125, 255, 255, 255, 255, -88.8158035278)
	create_npc('player/ct_gign', 'npc_teleport_nightfever 545 8551 79', 1, 2377.79199219, 1529.48461914, 128.03125, 255, 255, 255, 255, -136.987976074)
	create_npc('player/ct_gign', 'npc_sonic_nightfever', 1, -446.980194092, 3439.20849609, 32.03125, 255, 255, 255, 255, -90.0)
	create_npc('player/elis/gb/goblin.mdl', 'npc_tenji_nightfever', 1, 1410.64746094, 2853.8527832, 312.03125, 255, 0, 0, 255, 45)
	create_npc('player/hhp227/miku/miku', 'npc_reisen_nightfever', 2, 1840.04431152, 3489.38134766, 312.03125, 255, 255, 255, 255, 0.292468428612)
	create_npc('props/cs_office/vending_machine', 'npc_robot1_nightfever', 0, 689.889343262, 983.655639648, 17.03125, 255, 255, 255, 255, -1.1782553196)
	create_npc('props/cs_assault/ticketmachine.mdl', 'npc_ticket_nightfever', 0, -961.781677246, 439.682373047, 32.03125, 255, 125, 0, 255, 90)
	if str(sv('today')) == "day":
		create_npc('player/slow/napalm_atc/slow.mdl', 'npc_inventor_nightfever', 1, -713.125549316, 2213.68286133, 16.03125, 255, 255, 255, 255, -89.548210144)
		create_npc('player/ct_sas', 'npc_world_nightfever', 1, -1109.44555664, 1519.79125977, 32.03125, 255, 255, 255, 255, -1.19213652611)
	if str(sv('today')) == "night":
		ent = es.createentity("light_dynamic")
		es.entitysetvalue(ent, "brightness", 1)
		es.entitysetvalue(ent, "style", 4)
		es.entitysetvalue(ent, "distance", 600.0)
		es.entitysetvalue(ent, "spotlight_radius", 600.0)
		es.spawnentity(ent)
		es.set("gaylight_ent", ent)
		est.setentitycolor(ent, 255, 0, 255, 255)
		est.entteleport(ent, -1349, 1577, 108)
		create_npc('player/ct_gsg9', 'npc_gaygate_nightfever', 1, -1127.9732666, 1525.55249023, 32.03125, 255, 0, 125, 255, -0)
		create_npc('combine_soldier', 'npc_gay1_nightfever', 27, -1132.38098145, 1728.05407715, 44.03125, 255, 255, 255, 255, -49.2009963989, 2)
		create_npc('combine_soldier', 'npc_gay2_nightfever', 27, -1139.23876953, 1683.26330566, 44.03125, 255, 255, 255, 255, 30.5710048676, 2)
		yeah = create_npc('combine_super_soldier', 'npc_gay3_nightfever', 27, -1195.43664551, 1714.60961914, 44.03125, 255, 255, 255, 255, -15.9369974136, 2)
		es.emitsound("entity", yeah, "zeisenproject_-1/autosounds/club.mp3", 1.0, 1.0, 99)
		es.emitsound("entity", yeah, "zeisenproject_-1/autosounds/club.mp3", 1.0, 1.0, 99)
		es.emitsound("entity", yeah, "zeisenproject_-1/autosounds/club.mp3", 1.0, 1.0, 99)
		es.emitsound("entity", yeah, "zeisenproject_-1/autosounds/club.mp3", 1.0, 1.0, 99)
		es.emitsound("entity", yeah, "zeisenproject_-1/autosounds/club.mp3", 1.0, 1.0, 99)
		es.emitsound("entity", yeah, "zeisenproject_-1/autosounds/club.mp3", 1.0, 1.0, 99)
		es.emitsound("entity", yeah, "zeisenproject_-1/autosounds/club.mp3", 1.0, 1.0, 99)
		es.emitsound("entity", yeah, "zeisenproject_-1/autosounds/club.mp3", 1.0, 1.0, 99)
		create_npc('combine_soldier', 'npc_gay4_nightfever', 27, -1201.2019043, 1348.07434082, 44.03125, 255, 255, 255, 255, 20.8250274658, 2)
		create_npc('combine_soldier', 'npc_gay5_nightfever', 27, -1211.63903809, 1411.8223877, 44.03125, 255, 255, 255, 255, -125.232971191, 2)
		create_npc('combine_soldier', 'npc_gay6_nightfever', 27, -1311.59814453, 1405.5670166, 44.03125, 255, 255, 255, 255, 48.1710319519, 2)
		create_npc('combine_soldier', 'npc_gay7_nightfever', 27, -1236.3840332, 1494.52990723, 44.03125, 255, 255, 255, 255, -107.676925659, 2)
		create_npc('combine_soldier', 'npc_gay8_nightfever', 27, -1396.19030762, 1388.56140137, 44.03125, 255, 255, 255, 255, 46.1470565796, 2)
		create_npc('combine_soldier', 'npc_gay9_nightfever', 27, -1339.41064453, 1519.63867188, 44.03125, 255, 255, 255, 255, -65.7889404297, 2)
		create_npc('combine_super_soldier', 'npc_gay10_nightfever', 27, -1281.26831055, 1595.83032227, 44.03125, 255, 255, 255, 255, 16.9310684204, 2)
		create_npc('combine_super_soldier', 'npc_gay11_nightfever', 27, -1219.51403809, 1580.85620117, 44.03125, 255, 255, 255, 255, 165.15899658, 2)
		create_npc('combine_super_soldier', 'npc_gay12_nightfever', 27, -1234.5690918, 1646.08251953, 44.03125, 255, 255, 255, 255, -106.75297546, 2)
		create_npc('player/techknow/paranoya/paranoya', 'npc_junpei_nightfever', 1, -1136.3536377, 1825.78466797, 16.03125, 255, 255, 255, 255, 0.351231336594)
		
def boss_skill(username, skillname):
	esc.msg("%s 보스#255,255,255가 %s 스킬#255,255,255을 시전했습니다!" %(username, skillname))

def getgametime():
	index = es.createentity("env_particlesmokegrenade")
	gametime = es.getindexprop(index, "ParticleSmokeGrenade.m_flSpawnTime")
	es.remove(index)
	return gametime

def get_z_max(userid):
	ang = es.getplayerprop(userid, 'CBaseEntity.m_angRotation').split(",")
	ang[0] = es.getplayerprop(userid, "CCSPlayer.m_angEyeAngles[0]")
	the_id = int(sv('m1_id'))
	x,y,z = es.getplayerlocation(userid)
	es.setpos(the_id, x, y, (z + 65))
	es.setang(the_id, -90, ang[1], ang[2])
	es.prop_dynamic_create(the_id, "blackout.mdl")
	last_give = int(sv('eventscripts_lastgive'))
	es.entitysetvalue(last_give, "classname", "delete_zkf")
	get_location = es.getindexprop(last_give, "CBaseEntity.m_vecOrigin").split(",")
	get_location[2] = float(get_location[2]) - 80
	toa = "%s,%s,%s" %(get_location[0], get_location[1], get_location[2])
	remove("delete_zkf")
	return toa

def none_select(userid, choice, popupname):
	pass

def endthegame():
	#s.server.cmd('sm_cancelvote')
	es.server.cmd('es_xdelayed 8 sm_map %s' %(sv('sm_nextmap')))

def getEyeLocation(userid):
	return tuple(es.getplayerprop(userid, 'CBasePlayer.localdata.m_vecViewOffset[' + str(x) + ']') + y for x, y in enumerate(es.getplayerlocation(userid)))

def getViewCoord(userid):
	es.prop_dynamic_create(userid, "blackout.mdl")
	es.setindexprop(sv('eventscripts_lastgive'), "CDynamicProp.baseclass.baseclass.baseclass.m_CollisionGroup", 2)
        location = es.getindexprop(sv('eventscripts_lastgive'), 'CBaseEntity.m_vecOrigin')
        es.remove(sv('eventscripts_lastgive'))
        return location

def isWallBetween(userid, userid2):
	#ok_userid = es.getuserid()
	start_location = getEyeLocation(userid)
	x,y,z = es.getplayerlocation(userid)
	#es.setpos(ok_userid, x, y, z)
	end_location = getEyeLocation(userid2)
	viewCoord(userid, end_location)
	view_location = map(float, getViewCoord(userid).split(','))
	result = True
	for x in (0, 1, 2):
		if not min(start_location[x], end_location[x]) <= view_location[x] <= max(start_location[x], end_location[x]):
			result = False
			break
	return result

def getViewAngle(userid):
        myRotation  = es.getplayerprop(userid, "CBaseEntity.m_angRotation").split(',')[2]
        myEyeAngle0 = es.getplayerprop(userid, _eyeangle % 0)
        myEyeAngle1 = es.getplayerprop(userid, _eyeangle % 1)
        return (myEyeAngle0, (myEyeAngle1 + 360) if myEyeAngle1 < 0 else myEyeAngle1, float(myRotation))

def viewCoord(userid, value):
	myLocation = getEyeLocation(userid)
	myVector = es.createvectorstring(myLocation[0], myLocation[1], myLocation[2])
	theVector = es.createvectorstring(value[0], value[1], value[2])
	ourVector = es.createvectorfrompoints(myVector, theVector)
	ourVector = es.splitvectorstring(ourVector)
	myViewAngle = getViewAngle(userid)
	ourAtan = math.degrees(math.atan(float(ourVector[1]) / float(ourVector[0])))
	if float(ourVector[0]) < 0:
		RealAngle = ourAtan + 180
	elif float(ourVector[1]) < 0:
		RealAngle = ourAtan + 360
	else:
		RealAngle = ourAtan
	yAngle = RealAngle
	xAngle = 0 - math.degrees(math.atan(ourVector[2] / math.sqrt(math.pow(float(ourVector[1]), 2) + math.pow(float(ourVector[0]), 2))))
	es.server.cmd('es_xsetang %s %s %s %s' % (userid, xAngle, yAngle, myViewAngle[2]))

def gethandlefromindex(handle):
	return es.entitygetvalue(index, "handle")

def getindexfromhandle(handle):
	for index in es.getEntityIndexes():
		if es.entitygetvalue(index, "handle") == handle:
			return index
	return None

def someone():
        for userid in es.getUseridList():
                return userid
def remove(entityname):
	userid = someone
	es.fire(userid, entityname, "kill")

def getweaponcolor(userid):
        color = es.getindexprop(userid, "CBaseEntity.m_clrRender")
        return tuple(int(x) for x in (color & 0xff, (color & 0xff00) >> 8, (color & 0xff0000) >> 16, (color & 0xff000000) >> 24))

def pushto(userid,attacker):
	lx,ly,lz = es.getplayerlocation(player)
	x,y,z = es.getplayerlocation(attacker)
	if abs(lx - x) <= size and abs(ly - y) <= size and abs(lz - z) <= size:
		if lx > x:
			tx = -(size - abs(lx - x)) / 4 if (size - abs(lx - x)) / 4 < 300 else -300
		else:
			tx = (size - abs(lx - x)) / 4 if -(size - abs(lx - x)) / 4 > -300 else 300
		if ly > y:
			ty = -(size - abs(ly - y)) / 4 if (size - abs(ly - y)) / 4 < 300 else -300
		else:
			ty = (size - abs(ly - y)) / 4 if -(size - abs(ly - y)) / 4 > -300 else 300
		if lz > z:
			tz = -(size - abs(ly - z)) / 4 if (size - abs(ly - z)) / 4 < 300 else -300
		else:
			tz = (size - abs(ly - z)) / 4 if -(size - abs(ly - z)) / 4 > -300 else 300
		es.setplayerprop(player, 'CBasePlayer.localdata.m_vecBaseVelocity', '%s,%s,%s'%(tx, ty, tz))

def getclantag(userid):
	return SPEPlayer(userid).clantag

def create_dynamic(model, x, y, z):
	userid = es.getUseridList()[0]
	es.server.cmd('es_xprop_dynamic_create %s "%s"' %(userid, model))
	est.entteleport(sv('eventscripts_lastgive'), x, y, z)
	return sv('eventscripts_lastgive')

def getuseridfromhandle(handle):
	for userid in es.getUseridList():
		if es.getplayerhandle(userid) == handle: return userid
	return None

def change_team(userid, team):
        es.changeteam(userid, team)
        if team == 3: usermsg.showVGUIPanel(userid, 'class_ct', False)
        if team == 2: usermsg.showVGUIPanel(userid, 'class_ter', False)

def deleting_bomb(userid):
	return es.getplayerprop(userid, 'CCSPlayer.m_bIsDefusing') % 2

def centermsg(what):
	for userid in es.getUseridList():
		usermsg.centermsg(userid, what)

def testprint():
	#es.set("effect_show", 1)
	es.set("allfade", 1)
	est.play("#h", "beatfeast/opening.mp3")
	story_hudmsg_x("Project Leader │ Zeisen", 0, 0.5, 0)
	gamethread.delayed(4, story_hudmsg_x, ("Original │ I Wanna Kill The Kamilia Game", 0.9, 0.3, 1, 0.8))
	gamethread.delayed(7.8, story_hudmsg_x, ("Coding Addon │ Eventscripts By Mattie", 0.8, 0.2, 2, 0.4))
	gamethread.delayed(11.3, story_hudmsg_x, ("Tester │ Zeisen Feast Group Members", 0, 0.7, 3, 0.5))
	gamethread.delayed(18, think, ("…", "The Guy"))
	gamethread.delayed(21, think, ("！", "The Guy"))
	gamethread.delayed(26, story_hudmsg_x, ("Opening Music │ ヒゲドライバー", 0.3, 0.5, 4, 0.65))
	gamethread.delayed(31, story_hudmsg_x, ("Speical Thanks │ Kamilia", 0.2, 0.65, 5, 0.2))
	gamethread.delayed(35, story_hudmsg_x, ("Zeisen Server List │ Project 1, 2, 3, -1", 0.9, 0.65, 5, 0.8))
	gamethread.delayed(40, story_hudmsg_x, ("A Boy “ What are you doing here?! ”", 0.2, 0.25, 6, 0.3))
	gamethread.delayed(45, story_hudmsg_x, ("The Guy “ I Wanna Beat The Feast. ”", 0.6, 0.5, 7, 0.45))
	gamethread.delayed(50, story_hudmsg_x, ("A Boy “ Are you sure? not safely!! ”", 0.3, 0.35, 8, 0.3))
	gamethread.delayed(55, story_hudmsg_x, ("The Guy “ No Problem. I must do revenge. ”", 0.6, 0.5, 9, 0.45))
	gamethread.delayed(60, story_hudmsg_x, ("A Boy “ Huh?! Also, You can't beat them alone. Guy! ”", 0.3, 0.35, 10, 0.3))
	gamethread.delayed(65, story_hudmsg_x, ("The Guy “ Not alone. I make friends for beat them. ”", 0.6, 0.5, 11, 0.45))
	gamethread.delayed(70, story_hudmsg_x, ("A Boy “ ... I can't your break stubbornness. good luck. ”", 0.3, 0.35, 12, 0.3))
	gamethread.delayed(80, story_hudmsg_x, ("The Guy “ ... I Just Wanna Beat The Feast. ”", 0.6, 0.5, 11, 0.45))
	gamethread.delayed(83, center_msg, ("I WANNA BEAT THE FEAST"))
	gamethread.delayed(86, center_msg, ("I WANNA BEAT THE FEAST(Version 0.001 Alpha)"))
	gamethread.delayed(90, center_msg, ("Show Your Skill..."))
	gamethread.delayed(94, story_hudmsg_x, ("Project Leader │ Zeisen", 0, 0.5, 0))
	gamethread.delayed(99, story_hudmsg_x, ("Original │ I Wanna Kill The Kamilia Game", 0.9, 0.3, 1, 0.8))
	gamethread.delayed(105, story_hudmsg_x, ("Opening Music │ ヒゲドライバー", 0.3, 0.5, 4, 0.65))
	gamethread.delayed(110, story_hudmsg_x, ("Speical Thanks │ Kamilia", 0.2, 0.65, 5, 0.2))
	#gamethread.delayed(0.25, effect_hudmsg, ('＊ ', 0.74, 0.6, 255, 255, 0))

def think(themsg, username):
	for userid in es.getUseridList():
		gamethread.delayed(0.01, usermsg.hudmsg, (userid, "┌─────┐ ", 11, 0, 0.35))
		gamethread.delayed(0.02, usermsg.hudmsg, (userid, "│　　　　　│ ", 12, 0, 0.375))
		gamethread.delayed(0.03, usermsg.hudmsg, (userid, "│　　%s　　│ " %(themsg), 13, 0, 0.4))
		gamethread.delayed(0.04, usermsg.hudmsg, (userid, "│　　　　　│ ", 14, 0, 0.425))
		gamethread.delayed(0.05, usermsg.hudmsg, (userid, "└─────┘ ", 15, 0, 0.45))
		gamethread.delayed(0.05, usermsg.hudmsg, (userid, "┘(%s)" %(username), 16, 0, 0.475))

def story_hudmsg_x(msg, start_x=0.4, end_x=0.4, C=0, start_y=0.4):
	if start_x != end_x:
		es.set("print_a", start_x)
		A = float(sv('print_a'))
		if A <= end_x:
			A += 0.01
			es.set("print_a", A)
			for userid in es.getUseridList():
				usermsg.hudmsg(userid, msg, C, A, start_y, fadeout=0.3, holdtime=2.7)
			if A <= end_x: gamethread.delayed(0.01, story_hudmsg_loop_x, (msg, end_x, start_y, C, "+"))
		if A >= end_x: 
			A -= 0.01
			es.set("print_a", A)
			for userid in es.getUseridList():
				usermsg.hudmsg(userid, msg, C, A, start_y, fadeout=0.3, holdtime=2.7)
			if A >= end_x: gamethread.delayed(0.01, story_hudmsg_loop_x, (msg, end_x, start_y, C, "-"))

def story_hudmsg_y(msg, start_y=0.4, end_y=0.4, C=0, start_x=0.4):
	if start_y != end_y:
		es.set("print_a", start_y)
		A = float(sv('print_a'))
		if A <= end_y:
			A += 0.01
			es.set("print_a", A)
			for userid in es.getUseridList():
				usermsg.hudmsg(userid, msg, C, start_x, A, fadeout=0.3, holdtime=2.7)
			if A <= end_y: gamethread.delayed(0.01, story_hudmsg_loop_y, (msg, start_x, end_y, C, "+"))
		if A >= end_y: 
			A -= 0.01
			es.set("print_a", A)
			for userid in es.getUseridList():
				usermsg.hudmsg(userid, msg, C, start_x, A, fadeout=0.3, holdtime=2.7)
			if A >= end_y: gamethread.delayed(0.01, story_hudmsg_loop_y, (msg, start_x, end_y, C, "-"))

def story_hudmsg_loop_x(msg, end_x, y, C, what):
	A = float(sv('print_a'))
	if what == "+":
		A += 0.01
		es.set("print_a", A)
		for userid in es.getUseridList():
			usermsg.hudmsg(userid, msg, C, A, y, fadeout=0.3, holdtime=2.7)
		if A <= end_x: gamethread.delayed(0.01, story_hudmsg_loop_x, (msg, end_x, y, C, "+"))
	if what == "-":
		A -= 0.01
		es.set("print_a", A)
		for userid in es.getUseridList():
			usermsg.hudmsg(userid, msg, C, A, y, fadeout=0.3, holdtime=2.7)
		if A >= end_x: gamethread.delayed(0.01, story_hudmsg_loop_x, (msg, end_x, y, C, "-"))

def story_hudmsg_loop_y(msg, end_x, y, C, what):
	A = float(sv('print_a'))
	if what == "+":
		A += 0.01
		es.set("print_a", A)
		for userid in es.getUseridList():
			usermsg.hudmsg(userid, msg, C, y, A, fadeout=0.3, holdtime=2.7)
		if A <= end_x: gamethread.delayed(0.01, story_hudmsg_loop_y, (msg, y, end_x, C, "+"))
	if what == "-":
		A -= 0.01
		es.set("print_a", A)
		for userid in es.getUseridList():
			usermsg.hudmsg(userid, msg, C, y, A, fadeout=0.3, holdtime=2.7)
		if A >= end_x: gamethread.delayed(0.01, story_hudmsg_loop_y, (msg, y, end_x, C, "-"))

def center_msg(msg):
	for userid in es.getUseridList():
		usermsg.centermsg(userid, msg)

def create_npc(model, name, seq, x, y, z, red, green, blue, alpha, ang, group=5):
	exisc = es.getentityindex(name)
	if exisc > 0: es.remove(exisc)
	npcindex = est.makeentity("cycler", model, x, y, z)
	es.entitysetvalue(npcindex, "classname", name)
	if seq:
		randseq = random.randint(1,250)
		randseq = randseq / 100
		gamethread.delayed(randseq, es.entitysetvalue, (npcindex, "Sequence", seq))
	es.setindexprop(npcindex, "CAI_BaseNPC.baseclass.baseclass.baseclass.baseclass.baseclass.m_CollisionGroup", group)
	es.setindexprop(npcindex, "CAI_BaseNPC.m_lifeState", 0)
	est.setentitycolor(npcindex, red, green, blue, alpha)
	es.setindexprop(npcindex, "CBaseEntity.m_angRotation", "0,%s,0" %(ang))
	return npcindex
