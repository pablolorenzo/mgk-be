import  glovalService  from './global'
function getServices() {
  const requestOptions = {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json;charset=UTF-8', 
      'Access-Control-Allow-Origin': '*',
    },
    credentials: 'include'
  };

  return fetch(`/api/services`, requestOptions)
  .then(glovalService.handleResponse);
}

export const ServicesService = {
  getServices,
};
