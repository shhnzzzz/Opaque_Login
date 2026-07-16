import api from "../api/api";

export async function registerStart(data) {

    const response = await api.post(
        "/auth/register/start",
        data
    );

    return response.data;
}

export async function registerFinish(data) {

    const response = await api.post(
        "/auth/register/finish",
        data
    );

    return response.data;
}