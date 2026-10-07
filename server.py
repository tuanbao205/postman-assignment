import json
from http.server import BaseHTTPRequestHandler, HTTPServer
courses={1:{"id":1,"name":"Kiem thu phan mem","credits":3}}
next_id=2
class Handler(BaseHTTPRequestHandler):
 def respond(self,status,data):
  self.send_response(status); self.send_header("Content-Type","application/json; charset=utf-8"); self.end_headers(); self.wfile.write(json.dumps(data,ensure_ascii=False).encode())
 def do_GET(self):
  if self.path=="/courses": return self.respond(200,list(courses.values()))
  try: item=courses[int(self.path.removeprefix("/courses/"))] if self.path.startswith("/courses/") else None
  except (ValueError,KeyError): item=None
  self.respond(200,item) if item else self.respond(404,{"error":"Course not found"})
 def save(self,create):
  global next_id
  try:
   data=json.loads(self.rfile.read(int(self.headers.get("Content-Length",0))))
   if not isinstance(data,dict) or not isinstance(data.get("name"),str) or not data["name"].strip() or type(data.get("credits")) is not int or data["credits"]<=0: raise ValueError()
  except (ValueError,TypeError): return self.respond(400,{"error":"name and positive integer credits required"})
  if create:
   if self.path!="/courses": return self.respond(404,{"error":"Not found"})
   i=next_id; next_id+=1
  else:
   try: i=int(self.path.removeprefix("/courses/")) if self.path.startswith("/courses/") else -1
   except ValueError: i=-1
   if i not in courses: return self.respond(404,{"error":"Course not found"})
  courses[i]={"id":i,"name":data["name"],"credits":data["credits"]}; self.respond(201 if create else 200,courses[i])
 def do_POST(self): self.save(True)
 def do_PUT(self): self.save(False)
 def do_DELETE(self):
  try: i=int(self.path.removeprefix("/courses/")) if self.path.startswith("/courses/") else -1
  except ValueError: i=-1
  if i not in courses: return self.respond(404,{"error":"Course not found"})
  del courses[i]; self.respond(200,{"message":"Deleted","id":i})
print("API: http://127.0.0.1:8000",flush=True)
HTTPServer(("127.0.0.1",8000),Handler).serve_forever()
