import { readFileSync } from "fs";
import { defineConfig } from "vite";

export default defineConfig({
    plugins: [(await import("@vitejs/plugin-vue")).default()],
    server: {
        host: "127.0.0.1",
        port: 443,
        https: {
            key: readFileSync("./certs/private_key.pem"),
            cert: readFileSync(
                "./certs/fullchain.pem"
            ) /* openssl сертификат для localhost(127.0.0.1) на 1000 лет */,
        },
    },
});
