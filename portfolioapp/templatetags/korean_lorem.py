from django import template
from random import choice, sample

register = template.Library()

NEWJEANS_CONTENT = [
    # Member descriptions
    "뉴진스의 민지가 'Hype Boy' 뮤비에서 완벽한 비주얼을 선보였어요!",
    "해린의 상큼한 미소가 'Attention' 안무 포인트에 완벽히 어울려요.",
    "다니엘의 'OMG' 뮤비 속 댄스브레이크가 너무 멋졌어요!",
    "하니의 'Cookie' 가사 전달력이 정말 대단하다고 생각해요.",
    "혜인의 'Ditto' 퍼포먼스가 마음속 깊이 남아요.",
    
    # Song references
    "'Attention'으로 데뷔한 뉴진스의 음악은 정말 중독성이 강해요!",
    "'Hype Boy' 안무 포인트 따라하기 도전해보셨나요?",
    "'OMG' 뮤비 속 패션 아이템이 모두 품절되었다고 해요!",
    "'Ditto' 겨울 감성과 뉴진스의 목소리가 잘 어울려요.",
    "'Cookie' 가사가 귀엽지만 의미가 깊은 노래예요.",
    
    # Fan comments
    "뉴진스 멤버들 모두 실력과 비주얼이 완벽한 것 같아요!",
    "민지와 해린의 케미스트리가 정말 좋아요!",
    "다니엘의 댄스 실력이 점점 더 좋아지고 있어요!",
    "하니의 보컬이 'Ditto'에서 정말 빛났어요!",
    "혜인의 퍼포먼스 에너지가 무대를 완전히 사로잡아요!",
    
    # General praise
    "뉴진스 노래는 들을수록 중독성 있어요!",
    "뉴진스 안무는 따라하기 어렵지만 멋있어요!",
    "뉴진스 멤버들 각자 개성이 뚜렷해서 좋아요!",
    "뉴진스 뮤비는 볼 때마다 새로운 포인트가 발견돼요!",
    "뉴진스 패션 스타일이 정말 트렌디해요!",
]

@register.simple_tag
def newjeans_lorem(count=1):
    """Generates random NewJeans-related Korean text"""
    return ' '.join([choice(NEWJEANS_CONTENT) for _ in range(count)])

@register.simple_tag
def newjeans_members():
    """Returns random member names"""
    members = ["민지", "해린", "다니엘", "하니", "혜인"]
    return ', '.join(sample(members, 3)) + " 멤버가 특히 인기 많아요!"

@register.simple_tag
def newjeans_songs():
    """Returns random song titles"""
    songs = ["'Attention'", "'Hype Boy'", "'Cookie'", "'OMG'", "'Ditto'", "'Super Shy'", "'ETA'"]
    return ', '.join(sample(songs, 3)) + " 노래 추천드려요!"
