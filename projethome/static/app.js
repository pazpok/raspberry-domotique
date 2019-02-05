$(function () {
    socket = io.connect('http://' + document.domain + ':' + location.port);
    socket.on('connect', function () {
        $('#status').text('Connecté');
        socket.emit('client_connected', {
            data: 'New client!'
        });
    });

    socket.on('disconnect', function () {
        $('#status').text('Déconnecté');
    });

    socket.on('alert', function (data) {
        $('#status').text('Connecté');
        $('#content').append(data + "<br />");
    });

    socket.on('temp', function (data) {
        $('.deneme').text(data);
    });
});


const house = document.querySelector('#house');
const range = document.querySelector('#range');
const label = document.querySelector('#label');

const f = new Flipping();
const update = f.wrap(rooms => {
  const prevRooms = house.getAttribute('data-rooms');
  house.setAttribute('data-prev-rooms', prevRooms);
  house.setAttribute('data-rooms', rooms);
  
  label.setAttribute('data-prev-rooms', prevRooms);
  label.setAttribute('data-rooms', rooms);
  label.setAttribute('data-rooms-delta', rooms - prevRooms);
});

const range$ = Rx.Observable
  .fromEvent(range, 'input')
  .map(e => e.target.value)
  .startWith(6);

range$.subscribe(update);
