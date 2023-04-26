/** @odoo-module **/

import { WebClient } from "@web/webclient/webclient";
import { patch } from "web.utils";

patch(WebClient.prototype, "rocket_digital_sv.WebClient", {
    setup() {
        this._super();
        this.title.setParts({ zopenerp: "Rocket" });
    },
});