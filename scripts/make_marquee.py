import re

html_path = 'neo-flw-landing/index.html'
with open(html_path, 'r') as f:
    html = f.read()

# Extract the cards
start_marker = '<!-- Card 1: NEØ Smart Factory -->'
end_marker = '</div>\n        </div>\n      </section>'

start_idx = html.find(start_marker)
# Find the end of Card 4 (which is before the closing </div> of bento-grid)
# Let's search for "<!-- Card 4: FLOWPay -->" and its closing </div>
card4_marker = '<!-- Card 4: FLOWPay -->'
card4_idx = html.find(card4_marker)

# Find the end of card 4 by looking for the next </div> that closes portfolio-grid
# It's at line 911/912. The text is:
#                 processamento em tempo real, 100% fluído. Infraestrutura financeira do ecossistema.
#                 </p>
#               </div>
#             </div>
#           </div>

end_of_cards_str = '''                <p>
                  Gateway de pagamento próprio. PIX + cripto, processamento em
                  tempo real, 100% fluído. Infraestrutura financeira do
                  ecossistema.
                </p>
              </div>
            </div>'''

end_idx = html.find(end_of_cards_str) + len(end_of_cards_str)

cards_html = html[start_idx:end_idx]

# Remove scroll-reveal from cards inside marquee so they don't break the layout when scrolling
cards_html = cards_html.replace('scroll-reveal', '')

# Create the marquee structure
marquee_html = f'''<div class="marquee-container">
            <div class="marquee-track">
              {cards_html}
              <!-- CLONES FOR INFINITE SCROLL -->
              {cards_html}
            </div>
          </div>'''

# Replace the bento-grid with the marquee
bento_grid_start = '<div class="portfolio-grid bento-grid">'
full_bento_str = f'{bento_grid_start}\n            {cards_html}\n          </div>'

if full_bento_str in html:
    new_html = html.replace(full_bento_str, marquee_html)
else:
    # Fallback regex if exact string mismatch
    pattern = re.compile(r'<div class="portfolio-grid bento-grid">.*?</div>\s*</div>\s*</section>', re.DOTALL)
    new_html = html[:html.find(bento_grid_start)] + marquee_html + '\n        </div>\n      </section>' + html[html.find('</section>', html.find(bento_grid_start))+10:]
    # Wait, the fallback is risky. Let's just do a simpler replace.
    bento_start_idx = html.find(bento_grid_start)
    bento_end_idx = end_idx + html[end_idx:].find('</div>') + 6
    new_html = html[:bento_start_idx] + marquee_html + html[bento_end_idx:]

with open(html_path, 'w') as f:
    f.write(new_html)

print("Marquee HTML updated!")
