import http from 'k6/http';
import { sleep } from 'k6';

const baseUrl= "http://localhost:5050";
export default function () {
    var user_id = Math.floor(Math.random() * 200) + 1;
    http.get(`${baseUrl}/api/patient/${user_id}/chartevent`);
    sleep(3);
    http.get(`${baseUrl}/api/patient/${user_id}/labevent`);
}