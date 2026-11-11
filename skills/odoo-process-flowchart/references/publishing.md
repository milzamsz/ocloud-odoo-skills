# Sharing the page

The built folder is static: `index.html`, `process.js`, optional `media.js`, screenshots, and video.

Before publishing anything, ask the user:

- the host and the account it belongs to;
- whether access must be restricted, and how (identity-based access is preferred over a shared password);
- whether the screenshots or video contain client data. If they do, the page must not be public.

Pattern for a static host with a shared password and a large video (example: Cloudflare Pages):

- A middleware function checks a password held as a host secret and sets an HttpOnly, Secure cookie. It also sends `X-Robots-Tag: noindex`, and every file, the video included, sits behind it.
- Static hosts cap the size of a single file (Cloudflare Pages: 25 MiB). Keep the video in private object storage (for example R2) and stream it through a function that honours HTTP Range requests, so seeking works. Point `_video.src` in `media.js` at that function's path.
- Deploy with the host's CLI and record the project name, account, and how to rotate the password, in the delivery note but not in the skill or the page.

A four-digit or otherwise short shared password can be guessed: say so when the user picks one.
