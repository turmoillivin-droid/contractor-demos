/**
 * 1-Turn Batch Facebook DOM Extractor (Zero-Token Browser Script)
 * Evaluates the active Facebook Group feed in 1 turn instead of 30 clicks.
 * Extracts contractor name, phone numbers, post text, and direct image URLs.
 */

(() => {
  const saPhoneRegex = /(?:(?:\+27|0)\s*(?:[678][0-9])(?:\s*[0-9]){7})/;
  const articles = Array.from(document.querySelectorAll('div[role="feed"] div[role="article"], div[role="article"], div[data-ad-preview="message"]'));
  
  const results = [];
  const seenPhones = new Set();

  for (const article of articles) {
    const text = article.innerText || '';
    const phoneMatch = text.match(saPhoneRegex);
    if (!phoneMatch) continue;

    const rawPhone = phoneMatch[0].replace(/\s+/g, '');
    if (seenPhones.has(rawPhone)) continue;
    seenPhones.add(rawPhone);

    // Extract Author / Page Name
    const authorEl = article.querySelector('h2 a, h3 a, h4 a, strong a, a[role="link"]');
    const authorName = authorEl ? authorEl.innerText.trim() : 'Contractor';

    // Extract Post Text (first 400 chars)
    const caption = text.slice(0, 500).replace(/\n+/g, ' ');

    // Extract Images (high-res scontent only)
    const imgs = Array.from(article.querySelectorAll('img[src*="scontent"]'));
    const photoUrls = [];
    for (const img of imgs) {
      const src = img.getAttribute('src');
      if (src && !src.includes('p50x50') && !src.includes('s40x40') && !photoUrls.includes(src)) {
        photoUrls.push(src);
      }
    }

    if (photoUrls.length >= 2) {
      results.push({
        name: authorName,
        phone: rawPhone,
        caption: caption,
        photos: photoUrls.slice(0, 5)
      });
    }

    if (results.length >= 10) break;
  }

  return results;
})();
