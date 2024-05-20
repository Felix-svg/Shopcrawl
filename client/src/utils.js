
export const getWebsiteNameFromUrl = (url) => {
    try {
      const parsedUrl = new URL(url);
      const hostname = parsedUrl.hostname.replace('www.', '');
      // Extract domain name (e.g., "amazon", "jumia") from the hostname
      const domainParts = hostname.split('.');
      const websiteName = domainParts.length > 1 ? domainParts[1] : domainParts[0];
      return websiteName;
    } catch (error) {
      console.error('Error parsing URL:', error);
      return 'Unknown';
    }
  };
  