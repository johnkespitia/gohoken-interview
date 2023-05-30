# Frontend Challenge

1. **Resolve image loading issue:**
   - The images in the file `web/src/pages/index.tsx` should load successfully.
   - Verify that the images are not broken or displaying error placeholders.
   - Confirm that the images are being fetched from the correct source and have the correct URLs.

2. **Responsive image display:**
   - On desktop devices:
     - The images should be displayed in rows of three.
   - On mobile devices:
     - The images should be displayed in a single column.

3. **Prevent duplicate images:**
   - Check that duplicate images are not displayed in the list.
   - Verify that the logic prevents duplicate images from being loaded or rendered.

4. **Load visible images only:**
   - Implement a mechanism to load only the images that are visible to the user.
   - Images that are not currently visible on the screen should not be loaded or unnecessarily consume network resources.


# Backend Challenge
## Requirements

- [ ] The service should return a list of images from the remote service
- [ ] The service is pretty slow, so do the necessary optimizations to make it faster
- [ ] The API is really limited and only returns 10 images at a time. Implement a way to get more images from the remote service
- [ ] Navigating into /docs it doesn't show great documentation for the API. Improve documentation for the API


### Bonus Points
- [ ] Add some tests wherever you think it's necessary
- [ ] Add a Dockerfile to run the service
- [ ] Add a persistence layer to the cache
