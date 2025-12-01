"""
MkDocs 플러그인: 작성자 카드 자동 생성

사용법:
    문서에 {!author:username} 문법을 사용하면
    mkdocs.yml의 extra.authors에서 작성자 정보를 불러와
    자동으로 작성자 카드를 생성합니다.
"""

import re
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options


class AuthorCardPlugin(BasePlugin):
    """작성자 카드를 자동으로 생성하는 플러그인"""

    config_scheme = (
        ('enabled', config_options.Type(bool, default=True)),
    )

    def __init__(self):
        self.authors = {}

    def on_config(self, config, **kwargs):
        """설정 로드 시 작성자 정보 가져오기"""
        if 'extra' in config and 'authors' in config['extra']:
            self.authors = config['extra']['authors']
        return config

    def on_page_markdown(self, markdown, page, config, files, **kwargs):
        """마크다운 처리 시 {!author:username} 문법을 작성자 카드로 변환"""
        if not self.config.get('enabled', True):
            return markdown

        # {!author:username} 패턴 찾기
        pattern = r'\{!author:([a-zA-Z0-9_-]+)\}'
        
        def replace_author(match):
            author_id = match.group(1)
            
            # 작성자 정보 가져오기
            if author_id not in self.authors:
                return f'<!-- 작성자 "{author_id}"를 찾을 수 없습니다 -->'
            
            author = self.authors[author_id]
            name = author.get('name', author_id)
            github = author.get('github', '')
            email = author.get('email', '')
            bio = author.get('bio', '')
            avatar = author.get('avatar', '')
            
            # GitHub 아바타 URL 생성 (avatar가 없으면)
            if not avatar and github:
                # GitHub 사용자명으로 아바타 URL 생성
                avatar = f'https://github.com/{github}.png'
            elif avatar and not avatar.startswith('http'):
                # 상대 경로인 경우 절대 경로로 변환
                avatar = f'https://github.com/{avatar}'
            
            # 작성자 카드 마크다운 생성
            card_parts = ['!!! info "작성자"']
            
            # 아바타 이미지 추가
            if avatar:
                card_parts.append(
                    f'    <img src="{avatar}" alt="{name}" width="64" '
                    f'style="border-radius: 50%; float: left; margin-right: 16px; margin-bottom: 8px;" />'
                )
            
            # 이름과 링크
            if github:
                github_url = f'https://github.com/{github}'
                card_parts.append(f'    **[[{name}]]({github_url})**')
            else:
                card_parts.append(f'    **{name}**')
            
            # 소개
            if bio:
                card_parts.append(f'    {bio}')
            
            # 버튼들
            buttons = []
            if github:
                buttons.append(f'[GitHub](https://github.com/{github}){{ .md-button .md-button--primary }}')
            if email:
                buttons.append(f'[이메일](mailto:{email}){{ .md-button }}')
            
            if buttons:
                card_parts.append('')
                card_parts.extend([f'    {btn}' for btn in buttons])
            
            return '\n'.join(card_parts)
        
        # 패턴 치환
        markdown = re.sub(pattern, replace_author, markdown)
        
        return markdown

