function toggleButton(id,state){
  let button = document.getElementById(id);
  button.disabled = state;
}
const sio = io("http://localhost:8000");

sio.on('connect', () => {
  console.log('connected');
});

sio.on('init', (data) => {
  // const obj = JSON.parse(data);
  console.log("Initialized")
  toggleButton("m1",(!data.m1=="1"))
  toggleButton("m2",(!data.m2=="1"))
  toggleButton("m3",(!data.m3=="1"))

});

sio.on('disconnect', () => {
  console.log('disconnected');
});

sio.on('change',(id) =>{
    let button = document.getElementById(id);
    button.disabled = (button.disabled)?false:true;
})


