const express = require('express');
const app = express();
const port = 3000;

// GET 요청을 처리하는 라우트
app.get('/', (req, res) => {
  res.send('안녕하세요, 이것은 GET 요청의 응답입니다.');
});

// POST 요청을 처리하는 라우트
app.post('/', (req, res) => {
  console.log('POST 요청이 수신되었습니다.');
  res.send('POST 요청의 응답입니다.');
});

app.listen(port, () => {
  console.log(`서버가 포트 ${port}에서 실행 중입니다.`);
});