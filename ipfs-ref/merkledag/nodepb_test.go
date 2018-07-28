// Code generated by protoc-gen-gogo.
// source: node.proto
// DO NOT EDIT!

/*
Package merkledag is a generated protocol buffer package.

It is generated from these files:
	node.proto

It has these top-level messages:
	PBLink
	PBNode
*/
package merkledag

import testing "testing"
import math_rand "math/rand"
import time "time"
import code_google_com_p_gogoprotobuf_proto "github.com/jbenet/go-ipfs/Godeps/_workspace/src/code.google.com/p/gogoprotobuf/proto"
import testing1 "testing"
import math_rand1 "math/rand"
import time1 "time"
import encoding_json "encoding/json"
import testing2 "testing"
import math_rand2 "math/rand"
import time2 "time"
import code_google_com_p_gogoprotobuf_proto1 "github.com/jbenet/go-ipfs/Godeps/_workspace/src/code.google.com/p/gogoprotobuf/proto"
import math_rand3 "math/rand"
import time3 "time"
import testing3 "testing"
import fmt "fmt"
import math_rand4 "math/rand"
import time4 "time"
import testing4 "testing"
import code_google_com_p_gogoprotobuf_proto2 "github.com/jbenet/go-ipfs/Godeps/_workspace/src/code.google.com/p/gogoprotobuf/proto"
import math_rand5 "math/rand"
import time5 "time"
import testing5 "testing"
import fmt1 "fmt"
import go_parser "go/parser"
import math_rand6 "math/rand"
import time6 "time"
import testing6 "testing"
import code_google_com_p_gogoprotobuf_proto3 "github.com/jbenet/go-ipfs/Godeps/_workspace/src/code.google.com/p/gogoprotobuf/proto"

func TestPBLinkProto(t *testing.T) {
	popr := math_rand.New(math_rand.NewSource(time.Now().UnixNano()))
	p := NewPopulatedPBLink(popr, false)
	data, err := code_google_com_p_gogoprotobuf_proto.Marshal(p)
	if err != nil {
		panic(err)
	}
	msg := &PBLink{}
	if err := code_google_com_p_gogoprotobuf_proto.Unmarshal(data, msg); err != nil {
		panic(err)
	}
	for i := range data {
		data[i] = byte(popr.Intn(256))
	}
	if err := p.VerboseEqual(msg); err != nil {
		t.Fatalf("%#v !VerboseProto %#v, since %v", msg, p, err)
	}
	if !p.Equal(msg) {
		t.Fatalf("%#v !Proto %#v", msg, p)
	}
}

func TestPBLinkMarshalTo(t *testing.T) {
	popr := math_rand.New(math_rand.NewSource(time.Now().UnixNano()))
	p := NewPopulatedPBLink(popr, false)
	size := p.Size()
	data := make([]byte, size)
	for i := range data {
		data[i] = byte(popr.Intn(256))
	}
	_, err := p.MarshalTo(data)
	if err != nil {
		panic(err)
	}
	msg := &PBLink{}
	if err := code_google_com_p_gogoprotobuf_proto.Unmarshal(data, msg); err != nil {
		panic(err)
	}
	for i := range data {
		data[i] = byte(popr.Intn(256))
	}
	if err := p.VerboseEqual(msg); err != nil {
		t.Fatalf("%#v !VerboseProto %#v, since %v", msg, p, err)
	}
	if !p.Equal(msg) {
		t.Fatalf("%#v !Proto %#v", msg, p)
	}
}

func BenchmarkPBLinkProtoMarshal(b *testing.B) {
	popr := math_rand.New(math_rand.NewSource(616))
	total := 0
	pops := make([]*PBLink, 10000)
	for i := 0; i < 10000; i++ {
		pops[i] = NewPopulatedPBLink(popr, false)
	}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		data, err := code_google_com_p_gogoprotobuf_proto.Marshal(pops[i%10000])
		if err != nil {
			panic(err)
		}
		total += len(data)
	}
	b.SetBytes(int64(total / b.N))
}

func BenchmarkPBLinkProtoUnmarshal(b *testing.B) {
	popr := math_rand.New(math_rand.NewSource(616))
	total := 0
	datas := make([][]byte, 10000)
	for i := 0; i < 10000; i++ {
		data, err := code_google_com_p_gogoprotobuf_proto.Marshal(NewPopulatedPBLink(popr, false))
		if err != nil {
			panic(err)
		}
		datas[i] = data
	}
	msg := &PBLink{}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		total += len(datas[i%10000])
		if err := code_google_com_p_gogoprotobuf_proto.Unmarshal(datas[i%10000], msg); err != nil {
			panic(err)
		}
	}
	b.SetBytes(int64(total / b.N))
}

func TestPBNodeProto(t *testing.T) {
	popr := math_rand.New(math_rand.NewSource(time.Now().UnixNano()))
	p := NewPopulatedPBNode(popr, false)
	data, err := code_google_com_p_gogoprotobuf_proto.Marshal(p)
	if err != nil {
		panic(err)
	}
	msg := &PBNode{}
	if err := code_google_com_p_gogoprotobuf_proto.Unmarshal(data, msg); err != nil {
		panic(err)
	}
	for i := range data {
		data[i] = byte(popr.Intn(256))
	}
	if err := p.VerboseEqual(msg); err != nil {
		t.Fatalf("%#v !VerboseProto %#v, since %v", msg, p, err)
	}
	if !p.Equal(msg) {
		t.Fatalf("%#v !Proto %#v", msg, p)
	}
}

func TestPBNodeMarshalTo(t *testing.T) {
	popr := math_rand.New(math_rand.NewSource(time.Now().UnixNano()))
	p := NewPopulatedPBNode(popr, false)
	size := p.Size()
	data := make([]byte, size)
	for i := range data {
		data[i] = byte(popr.Intn(256))
	}
	_, err := p.MarshalTo(data)
	if err != nil {
		panic(err)
	}
	msg := &PBNode{}
	if err := code_google_com_p_gogoprotobuf_proto.Unmarshal(data, msg); err != nil {
		panic(err)
	}
	for i := range data {
		data[i] = byte(popr.Intn(256))
	}
	if err := p.VerboseEqual(msg); err != nil {
		t.Fatalf("%#v !VerboseProto %#v, since %v", msg, p, err)
	}
	if !p.Equal(msg) {
		t.Fatalf("%#v !Proto %#v", msg, p)
	}
}

func BenchmarkPBNodeProtoMarshal(b *testing.B) {
	popr := math_rand.New(math_rand.NewSource(616))
	total := 0
	pops := make([]*PBNode, 10000)
	for i := 0; i < 10000; i++ {
		pops[i] = NewPopulatedPBNode(popr, false)
	}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		data, err := code_google_com_p_gogoprotobuf_proto.Marshal(pops[i%10000])
		if err != nil {
			panic(err)
		}
		total += len(data)
	}
	b.SetBytes(int64(total / b.N))
}

func BenchmarkPBNodeProtoUnmarshal(b *testing.B) {
	popr := math_rand.New(math_rand.NewSource(616))
	total := 0
	datas := make([][]byte, 10000)
	for i := 0; i < 10000; i++ {
		data, err := code_google_com_p_gogoprotobuf_proto.Marshal(NewPopulatedPBNode(popr, false))
		if err != nil {
			panic(err)
		}
		datas[i] = data
	}
	msg := &PBNode{}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		total += len(datas[i%10000])
		if err := code_google_com_p_gogoprotobuf_proto.Unmarshal(datas[i%10000], msg); err != nil {
			panic(err)
		}
	}
	b.SetBytes(int64(total / b.N))
}

func TestPBLinkJSON(t *testing1.T) {
	popr := math_rand1.New(math_rand1.NewSource(time1.Now().UnixNano()))
	p := NewPopulatedPBLink(popr, true)
	jsondata, err := encoding_json.Marshal(p)
	if err != nil {
		panic(err)
	}
	msg := &PBLink{}
	err = encoding_json.Unmarshal(jsondata, msg)
	if err != nil {
		panic(err)
	}
	if err := p.VerboseEqual(msg); err != nil {
		t.Fatalf("%#v !VerboseProto %#v, since %v", msg, p, err)
	}
	if !p.Equal(msg) {
		t.Fatalf("%#v !Json Equal %#v", msg, p)
	}
}
func TestPBNodeJSON(t *testing1.T) {
	popr := math_rand1.New(math_rand1.NewSource(time1.Now().UnixNano()))
	p := NewPopulatedPBNode(popr, true)
	jsondata, err := encoding_json.Marshal(p)
	if err != nil {
		panic(err)
	}
	msg := &PBNode{}
	err = encoding_json.Unmarshal(jsondata, msg)
	if err != nil {
		panic(err)
	}
	if err := p.VerboseEqual(msg); err != nil {
		t.Fatalf("%#v !VerboseProto %#v, since %v", msg, p, err)
	}
	if !p.Equal(msg) {
		t.Fatalf("%#v !Json Equal %#v", msg, p)
	}
}
func TestPBLinkProtoText(t *testing2.T) {
	popr := math_rand2.New(math_rand2.NewSource(time2.Now().UnixNano()))
	p := NewPopulatedPBLink(popr, true)
	data := code_google_com_p_gogoprotobuf_proto1.MarshalTextString(p)
	msg := &PBLink{}
	if err := code_google_com_p_gogoprotobuf_proto1.UnmarshalText(data, msg); err != nil {
		panic(err)
	}
	if err := p.VerboseEqual(msg); err != nil {
		t.Fatalf("%#v !VerboseProto %#v, since %v", msg, p, err)
	}
	if !p.Equal(msg) {
		t.Fatalf("%#v !Proto %#v", msg, p)
	}
}

func TestPBLinkProtoCompactText(t *testing2.T) {
	popr := math_rand2.New(math_rand2.NewSource(time2.Now().UnixNano()))
	p := NewPopulatedPBLink(popr, true)
	data := code_google_com_p_gogoprotobuf_proto1.CompactTextString(p)
	msg := &PBLink{}
	if err := code_google_com_p_gogoprotobuf_proto1.UnmarshalText(data, msg); err != nil {
		panic(err)
	}
	if err := p.VerboseEqual(msg); err != nil {
		t.Fatalf("%#v !VerboseProto %#v, since %v", msg, p, err)
	}
	if !p.Equal(msg) {
		t.Fatalf("%#v !Proto %#v", msg, p)
	}
}

func TestPBNodeProtoText(t *testing2.T) {
	popr := math_rand2.New(math_rand2.NewSource(time2.Now().UnixNano()))
	p := NewPopulatedPBNode(popr, true)
	data := code_google_com_p_gogoprotobuf_proto1.MarshalTextString(p)
	msg := &PBNode{}
	if err := code_google_com_p_gogoprotobuf_proto1.UnmarshalText(data, msg); err != nil {
		panic(err)
	}
	if err := p.VerboseEqual(msg); err != nil {
		t.Fatalf("%#v !VerboseProto %#v, since %v", msg, p, err)
	}
	if !p.Equal(msg) {
		t.Fatalf("%#v !Proto %#v", msg, p)
	}
}

func TestPBNodeProtoCompactText(t *testing2.T) {
	popr := math_rand2.New(math_rand2.NewSource(time2.Now().UnixNano()))
	p := NewPopulatedPBNode(popr, true)
	data := code_google_com_p_gogoprotobuf_proto1.CompactTextString(p)
	msg := &PBNode{}
	if err := code_google_com_p_gogoprotobuf_proto1.UnmarshalText(data, msg); err != nil {
		panic(err)
	}
	if err := p.VerboseEqual(msg); err != nil {
		t.Fatalf("%#v !VerboseProto %#v, since %v", msg, p, err)
	}
	if !p.Equal(msg) {
		t.Fatalf("%#v !Proto %#v", msg, p)
	}
}

func TestPBLinkStringer(t *testing3.T) {
	popr := math_rand3.New(math_rand3.NewSource(time3.Now().UnixNano()))
	p := NewPopulatedPBLink(popr, false)
	s1 := p.String()
	s2 := fmt.Sprintf("%v", p)
	if s1 != s2 {
		t.Fatalf("String want %v got %v", s1, s2)
	}
}
func TestPBNodeStringer(t *testing3.T) {
	popr := math_rand3.New(math_rand3.NewSource(time3.Now().UnixNano()))
	p := NewPopulatedPBNode(popr, false)
	s1 := p.String()
	s2 := fmt.Sprintf("%v", p)
	if s1 != s2 {
		t.Fatalf("String want %v got %v", s1, s2)
	}
}
func TestPBLinkSize(t *testing4.T) {
	popr := math_rand4.New(math_rand4.NewSource(time4.Now().UnixNano()))
	p := NewPopulatedPBLink(popr, true)
	size2 := code_google_com_p_gogoprotobuf_proto2.Size(p)
	data, err := code_google_com_p_gogoprotobuf_proto2.Marshal(p)
	if err != nil {
		panic(err)
	}
	size := p.Size()
	if len(data) != size {
		t.Fatalf("size %v != marshalled size %v", size, len(data))
	}
	if size2 != size {
		t.Fatalf("size %v != before marshal proto.Size %v", size, size2)
	}
	size3 := code_google_com_p_gogoprotobuf_proto2.Size(p)
	if size3 != size {
		t.Fatalf("size %v != after marshal proto.Size %v", size, size3)
	}
}

func BenchmarkPBLinkSize(b *testing4.B) {
	popr := math_rand4.New(math_rand4.NewSource(616))
	total := 0
	pops := make([]*PBLink, 1000)
	for i := 0; i < 1000; i++ {
		pops[i] = NewPopulatedPBLink(popr, false)
	}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		total += pops[i%1000].Size()
	}
	b.SetBytes(int64(total / b.N))
}

func TestPBNodeSize(t *testing4.T) {
	popr := math_rand4.New(math_rand4.NewSource(time4.Now().UnixNano()))
	p := NewPopulatedPBNode(popr, true)
	size2 := code_google_com_p_gogoprotobuf_proto2.Size(p)
	data, err := code_google_com_p_gogoprotobuf_proto2.Marshal(p)
	if err != nil {
		panic(err)
	}
	size := p.Size()
	if len(data) != size {
		t.Fatalf("size %v != marshalled size %v", size, len(data))
	}
	if size2 != size {
		t.Fatalf("size %v != before marshal proto.Size %v", size, size2)
	}
	size3 := code_google_com_p_gogoprotobuf_proto2.Size(p)
	if size3 != size {
		t.Fatalf("size %v != after marshal proto.Size %v", size, size3)
	}
}

func BenchmarkPBNodeSize(b *testing4.B) {
	popr := math_rand4.New(math_rand4.NewSource(616))
	total := 0
	pops := make([]*PBNode, 1000)
	for i := 0; i < 1000; i++ {
		pops[i] = NewPopulatedPBNode(popr, false)
	}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		total += pops[i%1000].Size()
	}
	b.SetBytes(int64(total / b.N))
}

func TestPBLinkGoString(t *testing5.T) {
	popr := math_rand5.New(math_rand5.NewSource(time5.Now().UnixNano()))
	p := NewPopulatedPBLink(popr, false)
	s1 := p.GoString()
	s2 := fmt1.Sprintf("%#v", p)
	if s1 != s2 {
		t.Fatalf("GoString want %v got %v", s1, s2)
	}
	_, err := go_parser.ParseExpr(s1)
	if err != nil {
		panic(err)
	}
}
func TestPBNodeGoString(t *testing5.T) {
	popr := math_rand5.New(math_rand5.NewSource(time5.Now().UnixNano()))
	p := NewPopulatedPBNode(popr, false)
	s1 := p.GoString()
	s2 := fmt1.Sprintf("%#v", p)
	if s1 != s2 {
		t.Fatalf("GoString want %v got %v", s1, s2)
	}
	_, err := go_parser.ParseExpr(s1)
	if err != nil {
		panic(err)
	}
}
func TestPBLinkVerboseEqual(t *testing6.T) {
	popr := math_rand6.New(math_rand6.NewSource(time6.Now().UnixNano()))
	p := NewPopulatedPBLink(popr, false)
	data, err := code_google_com_p_gogoprotobuf_proto3.Marshal(p)
	if err != nil {
		panic(err)
	}
	msg := &PBLink{}
	if err := code_google_com_p_gogoprotobuf_proto3.Unmarshal(data, msg); err != nil {
		panic(err)
	}
	if err := p.VerboseEqual(msg); err != nil {
		t.Fatalf("%#v !VerboseEqual %#v, since %v", msg, p, err)
	}
}
func TestPBNodeVerboseEqual(t *testing6.T) {
	popr := math_rand6.New(math_rand6.NewSource(time6.Now().UnixNano()))
	p := NewPopulatedPBNode(popr, false)
	data, err := code_google_com_p_gogoprotobuf_proto3.Marshal(p)
	if err != nil {
		panic(err)
	}
	msg := &PBNode{}
	if err := code_google_com_p_gogoprotobuf_proto3.Unmarshal(data, msg); err != nil {
		panic(err)
	}
	if err := p.VerboseEqual(msg); err != nil {
		t.Fatalf("%#v !VerboseEqual %#v, since %v", msg, p, err)
	}
}

//These tests are generated by code.google.com/p/gogoprotobuf/plugin/testgen
