/*
 * URL Shortener
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * OpenAPI spec version: v1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator.
 * https://github.com/OpenAPITools/openapi-generator
 *
 * Generator version: 7.7.0-SNAPSHOT
 */


import http from "k6/http";
import { group, check, sleep } from "k6";

const BASE_URL = "http://api:8000";
// Sleep duration between successive requests.
// You might want to edit the value of this variable or remove calls to the sleep function on the script.
const SLEEP_DURATION = 0.1;
// Global variables should be initialized.

export default function() {
   
    group("/api/shorten", () => {

        // Request No. 1: get_short_link_api_shorten_post
        {
            let url = BASE_URL + `/api/shorten`;
            // TODO: edit the parameters of the request body.
            let body = {"url": "http://uri.com"};
            let params = {headers: {"Content-Type": "application/json", "Accept": "application/json"}};
            let request = http.post(url, JSON.stringify(body), params);

            check(request, {
                "Successful Response": (r) => r.status === 200
            });
        }
    });

    group("/{short_link}", () => {

        // Request No. 1: redirect__short_link__get
        {
            let urlb = BASE_URL + `/api/shorten`;
            // TODO: edit the parameters of the request body.
            let body = {"url": "http://uri.com"};
            let params = {headers: {"Content-Type": "application/json", "Accept": "application/json"}};
            let requestb = http.post(urlb, JSON.stringify(body), params);
            const shortLink = JSON.parse(requestb.body).short_link;
            let url = BASE_URL + `/${shortLink}`;
            let request = http.get(url);

            check(request, {
                "Successful Response": (r) => r.status === 200
            });
        }
    });

    group("/", () => {

        // Request No. 1: main_function__get
        {
            let url = BASE_URL + `/`;
            let request = http.get(url);

            check(request, {
                "Successful Response": (r) => r.status === 200
            });
        }
    });

}
