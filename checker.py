import requests


# List of WordPress site URLs
urls = [
    'https://example1.com',
    'https://example2.com',
    # Add more URLs as needed
]


def detect_wpml(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Check for common WPML indicators in HTML source or URL paths
            if 'wp-content/plugins/sitepress-multilingual-cms' in response.text or \
               'wp-content/plugins/sitepress-multilingual-cms' in response.url:
                return True
        return False
    except requests.RequestException:
        return False


valid_sites = []


for url in urls:
    if detect_wpml(url):
        valid_sites.append(url)
        print(f"WPML plugin detected on {url}")
    else:
        print(f"No WPML plugin detected or error for {url}")


# Save valid sites to a file
with open('valid_sites.txt', 'w') as file:
    for site in valid_sites:
        file.write(site + '\n')


print("Valid sites have been saved to valid_sites.txt")
